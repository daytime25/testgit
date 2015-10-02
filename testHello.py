#vi TestHello2.py
from nose.tools import with_setup
def Func1_setup():   
      print ('case 1 setup')
def Func1_teardown():
      print ('case 1 teardown')

@with_setup( Func1_setup, Func1_teardown )
def Test_func1():
      print ('Test 1')
      assert True
def Func2_setup():
      print ('case 2 setup')
def Func2_teardown():
      print ('case 2 teardown')
@with_setup( Func2_setup, Func2_teardown )
def Test_func2():
      print ('Test 2')
      assert True
