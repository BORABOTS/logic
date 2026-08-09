#1. Write a python program to add two numbers.

a=1
b=2
print(a+b)

#2. Write a python program to find remainder when a number is divided by z.

a= 100
b= 3
print("remender is: ", a%b)

#3. Check the type of variable assigned using input() function.

a=input('enter anything: ')
# this always shows 'str' every time(6,mm, 7.88)
print(type(a))

#4. Use comparison operator to find out whether ‘aʼ given variable is greater than ‘bʼ or not.
#Take a = 34 and b = 80

a= 34
b= 80
if a>b:
    print('a is greater')
else:
    print('b is greater')


#5. Write a python program to find an average of two numbers entered by the user.

a= int(input('enter value of a : '))
b= int(input('enter value of b : '))
average= (a+b)/2
print(average)

#6 Write a python program to calculate the square of a number entered by the user.

a= int(input('enter value to do a square: ' ))
sqr= a*a
sqr1= a**2
print(sqr1)
print(sqr)