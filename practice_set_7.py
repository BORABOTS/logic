#1. Write a program to print multiplication table of a given number using for loop.

a=int(input("Enter no to form table of it: "))
print(f"Table of {a}")
for i in range(1,11):
    print(a*i)

#2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
    #l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith('S'):
        print("Hello",name)

#3. Attempt problem 1 using while loop.

a=int(input("Enter no to form table of it: "))
print(f"Table of {a}")
count=1
while count<=10:
    print(a*count)
    count+=1

#4. Write a program to find whether a given number is prime or not.

n = int(input("Enter a number to check whether the following no is prime or not: "))

for i in range(2, n):
    if n % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")

#5. Write a program to find the sum of first n natural numbers using while loop.

n= int(input("Enter number: "))
i=1
sum=0

while i<=n:
    sum=sum+i
    i=i+1
print("Sum : ",sum)

#6. Write a program to calculate the factorial of a given number using for loop.

n=int(input("Enter number to find factorial: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
    i=i+1
print(f"Factorial of {n} is ",fact)

#7. Write a program to print the following star pattern.

#*
#***
#***** for n = 3
n = 3

for i in range(1, n + 1):
    for j in range(2 * i - 1):
        print("*", end="")
    print()

#8. Write a program to print the following star pattern:
#*
#**
#*** for n = 3

n = 3

for i in range(1, n + 1):
    for j in range( i ):
        print("*", end="")
    print()

#9. Write a program to print the following star pattern.
#***
#** for n= 3
#***
n = 3

for i in range(n):# i runs from (0,1,2)
    if i == 1:
        print("**")
    else:
        print("***")
        
#10. Write a program to print multiplication table of n using for loops in reversed order.

a=int(input("Enter no to form table of it: "))
print(f"Table of {a}")
for i in range(10,0,-1):
    print(a*i)
