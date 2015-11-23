# coding=gbk
from unittest import TestCase
from parsers import HtmlParser, PdfParser, PdfFileReader, DocConverter, MpdfParser
 
 
class TestHTMLParser(TestCase):
    def test_empty_page(self):
        parser = HtmlParser("")
        self.assertEqual(parser.get_links(), [])
        self.assertEqual(parser.get_text(), '')
 
    def test_text_no_tags(self):
        parser = HtmlParser(
            "some text"
        )
        self.assertEqual(parser.get_text(), "some text")
 
    def test_one_link(self):
        parser = HtmlParser(
            "<a href='http://abc.abc/'>text</a>"
        )
        self.assertEqual(parser.get_links(), ['http://abc.abc/'])
 
    def test_get_several_links(self):
        parser = HtmlParser(
            "<div><a href='http://abc.abc/'>text</a></div><a href='http://def.def/'></a><div><A HREF='q.html'>text</a></div>"
        )
        self.assertEqual(parser.get_links(), ['http://abc.abc/', 'http://def.def/', 'q.html'])
 
    def test_new_line_test(self):
        parser = HtmlParser(
            "<div><p>some text</p></div><div><a>another text</a></div>"
        )
        self.assertEqual(parser.get_text(), "some text\nanother text")
 
    def test_meta(self):
        parser = HtmlParser(
            "<meta content='text/html; charset=utf-8' http-equiv='Content-Type'>"
        )
        self.assertEqual(parser.get_meta(), ["text/html; charset=utf-8"])
 
    def test_meta_wrong(self):
        parser = HtmlParser(
            "<meta content='text/html; charset=utf-8' http-equiv='123'>"
        )
        self.assertEqual(parser.get_meta(), ["text/html; charset=utf-8"])
 
    def test_character_entity_reference(self):
        parser = HtmlParser(
            "&amp;&lt;&gt;"
        )
        self.assertEqual(parser.get_text(), "&<>")
 
    def test_numeric_character_reference(self):
        parser = HtmlParser(
            "&#931;&#0931;&#x3A3;&#x03A3;&#x3a3;"
        )
        self.assertEqual(parser.get_text(), "ΣΣΣΣΣ")
 
    def test_script(self):
        parser = HtmlParser("<script type='text/javascript'>var a = 1</script>")
        self.assertEqual(parser.get_text(), '')
 
    def test_img_alt(self):
        parser = HtmlParser(
            "<img alt='some text'></img>"
        )
        self.assertEqual(parser.get_text(), "some text")