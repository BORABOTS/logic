#1. Write a python program to add two numbers.

print(" Program to find sum of no a,b")
a=int(input("value of a: "))
b=int(input("value of b: "))
print("Sum = ",a+b)

#2. Write a python program to find remainder when a number is divided by z.

print("Program to find a/b plss input value!")
a= int(input("Enter value of a: "))
b= int(input("Enter value of b: "))
print("Remender is: ", a%b)

#3. Check the type of variable assigned using input() function.

a=input("Enter anything(str,int,float): ")
# this always shows 'str' every time(6,mm, 7.88)
print(type(a))

#4. Use comparison operator to find out whether ‘aʼ given variable is greater than ‘bʼ or not.
#Take a = 34 and b = 8

print("Program to find greater no choose (a,b): ")

a= int(input("Enter value of a: "))
b= int(input("Enter value of b: "))
if a>b:
    print('A is greater')
else:
    print('B is greater')


#5. Write a python program to find an average of two numbers entered by the user.

print("program to find average of no: ")
a= int(input('Enter value of a : '))
b= int(input('Enter value of b : '))
average= (a+b)/2
print(average)

#6 Write a python program to calculate the square of a number entered by the user.

a= int(input('Enter value to do a square: ' ))
sqr= a*a
sqr1= a**2
print(sqr1)
print(sqr)
