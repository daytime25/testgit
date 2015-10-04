from nose import with_setup
#from tee import shuzi
#from tee import below_f
from calc1 import Interpreter
import nose


def my_setup():
  print "为测试执行配置代码"

def my_teardown():
  print "为测试执行清理代码"

@with_setup(my_setup,my_teardown)
def test_token():    
    token=token('INTEGER, 3')
    
    
    
def  test_interpreter():
    interpreter = Interpreter('3*55*456-55')
    interpreter.get_next_token()
    

    
    



result=nose.run()