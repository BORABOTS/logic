'''l = {
    "hary":"10",
    "mohit":"7"
}
print(type(l))

a= int(input("k"))# alt + mouse click

print(l["harry"])#shift+ alt + arrow()
print(l["harry"])#shift+ alt + arrow()
a= int(input("k"))# alt + mouse click
a= int(input("k"))# alt + mouse click -> multiple line comment:
print(l["harry"])#shift+ alt + arrow()
print(l["harry"])#shift+ alt + arrow()
print(l["harry"])#shift+ alt + arrow()
print(l["harry"])#shift+ alt + arrow()'''
'''
class Employee:
    name= "harrry"
    language = "py"
    salary = 1200000
    def __init__(self, name, salary, language): # dunder method which is automatically  called
        self.name=name
        self.salary= salary
        self.language= language
        print("I am creating an object")
    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
    def greet(self):
       print("Good Morning!")'''

'''
    @staticmethod
    def greet():
        print("Good Morning!")
'''
        
#harry = Employee("rohan",12000,"js")
#harry.language="js"

'''harry.greet()
harry.getInfo()#same 
Employee.getInfo(harry)#same'''
#print(harry.name,harry.language,harry.salary)

'''class Employee:
    company="ITC"
    name="default name"
    def show(self):
        
        print(f"my name is {self.name}")

class Coder:
    language="python"
    def printlanguage(self):
        print(f"out of all the languages here is your language: {self.language}")

class Programmer(Employee,Coder):#multiple inheritance
    company="Itc infotech"

    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language.")

a=Employee()
b=Programmer()

b.show()
b.printlanguage()
b.showlanguage()
 
'''
'''class Employee:
    a=1

class Programmer(Employee):#multiple inheritance
    b=2
class Manager(Programmer):
    c=3


o=Manager()#multilevel inheritance

print(o.a,o.b,o.c)'''
'''class Employee:
    def __init_(self):
        print("constructor of Employee")
    a=1

class Programmer(Employee):#multiple inheritance
    def __init_(self):
        print("constructor of Programmer")
    b=2
class Manager(Programmer):
    def __init_(self):
        super().__init__()
        print("constructor of Manager")
    c=3


o=Manager()# Use of super method

print(o.a,o.b,o.c)'''
class Employee():
    a=1
    @classmethod#it is a decoretor used to creater a class method
    def show(cls):
        print(f"the class attribute if {cls.a}")
    @property
    def name(self):
        return self.name
b=Employee()
b.a=23
b.show()
b.name="Harry"
print(b.name)
