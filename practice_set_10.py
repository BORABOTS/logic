# OOPS
#1. Create a class “Programmer” for storing information of few programmers working at
#Microsoft.

class Programmer():
    def greet(self):
        print("nice to see you! ")
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary= salary

r= Programmer("rohan",1, 1200)
print(r.name,r.id,r.salary)
h= Programmer("rohan",2, 1289)
print(h.name,h.id,h.salary)
l= Programmer("shyam",3, 1267)
print(l.name,l.id,l.salary)

#2. Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator():
    def __init__(self,n):
        self.n=n

    def square(self):
        square=self.n*self.n
        print(f"the square of no is {square}")

    def cube(self):

        cube=self.n*self.n*self.n
        print(f"the square of no is {cube}") 

    def square_root(self):

        square_root=(self.n**1/2)
        print(f"the square of no is {square_root}") 

print("this is a calculator")
n=int(input("enter n: "))
h= Calculator(n)
h.square()
h.cube()
h.square_root()

#3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
#‘object.a = 0ʼ. Does this change the class attribute?

class Attribute:
    a=4
o=Attribute()
print(o.a)# print the class attribute because instance attribute is 
#not present
o.a= 0# instance attribute is set
print(o.a)#printes the instance attribute 
print(Attribute.a)#prints the class attribute

#4. Add a static method in problem 2, to greet the user with hello.
class Problem:
    @staticmethod    #using static method we don't need to create an obj(self)
    def greet():
        print("hello there! ")
a=Problem()
a.greet()
#5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
#fare information of train running under Indian Railways.

from random import randint
class Train:
    def __init__(self, no, f , t):
        self.no = no
        self.f= f
        self.t= t

    def book(self):
        print(f"Ticket is booked in tain no: {self.no} from {self.f} to {self.t}")

    def getstatus(self):
        print(f"Train no: {self.no} is running successfully.")

        pass
    def getFare(self):
        print(f" Ticket fare in  train no: {self.no} from {self.f} to {self.t} is {randint(222,5555)}")
        
a=Train(444, "rampur","Delhi")
a.book()
a.getstatus()
a.getFare()


#6. Can you change the self-parameter inside a class to something else (say “harry”)? Try
#changing self to “slf” or “harry” and see the effects.

from random import randint
class Train:
    def __init__(self, no, f , t):
        self.no = no
        self.f= f
        self.t= t

    def book(harry):#yes it will not change the output
        print(f"Ticket is booked in tain no: {harry.no} from {harry.f} to {harry.t}")

    def getstatus(self):
        print(f"Train no: {self.no} is running successfully.")

        pass
    def getFare(self):
        print(f" Ticket fare in  train no: {self.no} from {self.f} to {self.t} is {randint(222,5555)}")
        
a=Train(444, "rampur","Delhi")
a.book()
a.getFare()

