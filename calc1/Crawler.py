# coding=gbk
from queue import Queue
from parsers import HtmlParser
import urllib.request
import urllib.error
import re
import time


class Crawler:
    reached_urls = {} # список достигнутых ссылок
    queue = Queue() # очередь ссылок, формат: (ссылка, номер попытки, глубина)
    subdomain_set = set() # найденные поддомены
    inner_link_counter = 0
    outer_link_counter = 0
    error_counter = 0
    max_attempts = 2 # максимальное число попыток загрузки страницы
    max_depth = 2 # максимальная глубина обхода сайта
    sleep_time = 0 # задержка между загрузкой страниц в секундах (для msu.ru ставить 1)

    def __init__(self, start_url):
        self.host = self.get_host(start_url)
        self.reached_urls[start_url] = 0
        self.queue.put((start_url, 0, 0))

    def crawl(self):
        while not self.queue.empty():
            (url, attempt, depth) = self.queue.get()

            print((url, attempt, depth))

            if self.is_outer_url(url):
                self.outer_link_counter += 1
            elif self.is_subdomain_url(url):
                self.subdomain_set.add(self.get_subdomain_name(url))
            else:
                self.inner_link_counter += 1
                if depth >= self.max_depth:
                    continue

                content = self.get_page(url)
                if not content:
                    if attempt >= self.max_attempts:
                        self.error_counter += 1
                        continue
                    else:
                        self.queue.put((url, attempt+1, depth))
                        continue

                parser =HtmlParser(content)
                url_list = parser.get_links()

                for u in url_list:
                    if len(u) < 1:
                        continue
                    u = self.make_full_link(u)
                    if u not in self.reached_urls:
                        self.reached_urls[u] = depth+1
                        self.queue.put((u, 0, depth+1))

        print(self.reached_urls)
        print(self.queue.qsize())
        print("Subdomains:", self.subdomain_set)
        print("Inner links count:", self.inner_link_counter)
        print("Outer links count:", self.outer_link_counter)
        print("Unavailable pages count:", self.error_counter)

    def get_page(self, url):
        """
        Принимает url адрес страницы, пытается её скачать
        При успехе возвращается содержимое страницы
        При ошибке выводится информация об ошибке, возвращается None
        """
        try:
            time.sleep(self.sleep_time)
            return urllib.request.urlopen(url, timeout=5).read()
        except urllib.error.HTTPError as e:
            print(e)
            return None
        except BaseException as e:
            print(e)
            return None

    def make_full_link(self, url):
        """
        Из url создаётся полная ссылка
        Например, '/index.html' будет преобразовано в 'http://spbu.ru/index.html',
        если в качестве стартовой страницы был указан 'http://spbu.ru/'
        """

        if url[0] == '/':
            url = 'http://' + self.host + url
        return url

    def is_subdomain_url(self, url):
        """
        Проверяется, ссылается ли url на поддомен
        """
        return not self.is_outer_url(url) and \
            not re.match(r'^(http|https|ftp)://(www\.|)' + self.host.replace('.', '\.') + r'(/.*|:.*|)$', url)

    def get_subdomain_name(self, url):
        """
        Из url выделяется поддомен
        Например, из 'http://apmath.spbu.ru/123' будет выделено 'apmath',
        если в качестве стартовой страницы был указан 'http://spbu.ru/'
        """
        if not self.is_subdomain_url(url):
            return None

        start = url.find('//') + 2
        end = url.find(self.host, start) - 1
        return url[start:end]

    def is_outer_url(self, url):
        """
        Проверяется, ссылается ли url на внешний адрес
        """
        return not re.match(r'^(http|https|ftp)://([^/]+\.|)' + self.host.replace('.', '\.') + r'(/.*|:.*|)$', url)

    @staticmethod
    def get_host(url):
        """
        Из url выделяется хост (без "www")
        Например, 'http://www.spbu.ru/' преобразуется в 'spbu.ru'
        """
        start = url.find('//') + 2
        end = url.find('/', start)
        end = end if end > 0 else len(url)

        url = url[start:end]
        if url.find('www.') == 0:
            url = url[4:]

        return url


crawler = Crawler('http://spbu.ru/')
crawler.crawl()