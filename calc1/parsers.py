


class HtmlParser:
    def __init__(self,content):
        if content == "":
            content = '<div></div>'
        #content = content.decode('cp1251').encode('utf8')
        self.content = html.fromstring(content)
    def get_links(self):
        links = self.content.xpath('//a/@href')
        return(links)
    def get_meta(self):
        meta = self.content.xpath('//meta/@content')
        return(meta)
    def get_text(self):
        cleaner = Cleaner()
        cleaner.javascript = True
        cleaner.style = True
        alts = ''
        self.content = cleaner.clean_html(self.content)
        for br in self.content.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"
        for br in self.content.xpath("*//p"):
            br.tail = "\n" + br.tail if br.tail else "\n"
        text = self.content.text_content()
        '''
       for elem in self.content.iter():
           print(elem.tag)
           if self.content.xpath('//'+elem.tag+'/@alt') != []:
               alts += str(self.content.xpath('//'+elem.tag+'/@alt'))
       cont =  str(text) + str(alts)
       return(cont)
       '''
        return(text)
    def get_code(self):
        cleaner = Cleaner()
        cleaner.javascript = True
        cleaner.style = True
        encoding = char
        return(code)