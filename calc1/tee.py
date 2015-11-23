from Tkinter import *           # 导入 Tkinter 库
root=Tk()
class tee(object):
    """description of class"""
listb=Listbox(root)
listb2=Listbox(root)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
def below_f(t):
    return t<0

for item in range(6):
   y=2*item+1
   print y
for num in range(2,15):
   for i in range(2,num):
        if num%i==0:
            j=num/i
            print (num,i,j)
            break
        else:
            print (num,i);   
            
def shuzi(t):
    t = -10                    # Second Example
    while t > -11:
        print 'Current variable value :', t
    t = t+1
    if t == 55:
        return t 
 
listb.pack()
root.mainloop()  
   
class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

def function(args):
    pass
