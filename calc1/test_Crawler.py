from nose.tools import *

from Crawler import crawler
from Crawler import make_full_link,get_page,is_subdomain_url

import nose


def my_setup():
  print ("为测试执行配置代码")

def my_teardown():
  print ("为测试执行清理代码")


@with_setup(my_setup,my_teardown)

def test_subdomain(self):
    crawler=Crawler('http://spbu.ru/')
    self.assertEqual(crawler.make_full_link('/index.html'),"http://spbu.ru/index.html")  

def test_get_page(self):
    crawler=Crawler('http://spbu.ru/')
    get_page=get_page('http://spbu.ru/')
    self.assertEqual()

def test_make_full_link(self):
    crawler=Crawler('http://spbu.ru/')
    full_link=make_full_link('/index.html')
    assert_equal(crawler,"http://spbu.ru/index.html")

def test_is_subdomain_url(self):
    crawler=Crawler('http://spbu.ru/')
    issubdomainurl=is_subdomain_url('https')
    assert_equal(crawler,"http://spbu.ru/index.html")


result=nose.run()