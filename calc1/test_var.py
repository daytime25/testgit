from nose.tools import *
#from tee import shuzi
#from tee import below_f
from calc1 import Interpreter,Token
from Crawler import crawler
import nose


def my_setup():
  print ("为测试执行配置代码")

def my_teardown():
  print ("为测试执行清理代码")

@with_setup(my_setup,my_teardown)
def test_token():    
    tok=Token("INTEGER",3)
    assert_equal(tok.type,"INTEGER")
    assert_equal(tok.value,3)
    
    
    
def  test_interpreter():
    interpreter = Interpreter('3*55*456-55')
    interpreter.get_next_token()
   
def test_subdomain(self):
    crawler=Crawler('http://spbu.ru/')
    self.assertEqual(crawler.make_full_link('/index.html'),"http://spbu.ru/index.html")
 
result=nose.run()