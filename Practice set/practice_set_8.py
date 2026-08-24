#1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if a>b and a>c:
        print("A is greater")
    elif c>a and c>b:
        print("C is greater")
    elif b>a and b>c:
        print("B is greater") 
    elif a==b and b==c:
        print('A,B,C are equal!')
    else:
        print("Check the value you provided!")
a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))

greatest(a,b,c)


#2. Write a python program using function to convert Celsius to Fahrenheit.

def temp(c):
    print("Converted celsius to fahreenheit: ",(c*9/5)+32)
c=int(input("Enter temp in Celsius: "))

temp(c)

#3. How do you prevent a python print() function to print a new line at the end.

print("a")
print("a",end="") # it cannot print new line but works on the same line
print("a")

#4. Write a recursive function to calculate the sum of first n natural numbers.-

def sum(n):
    if n==1:
        return 1
    return sum(n-1) + n

n=int(input("enter n for sum: "))
print(sum(n))

#5. Write a python function to print first n lines of the following pattern. for n = 3
#***
#**
#*

def pattern(n):
    if n==0:
        return
    print('*'*n)
    pattern(n-1)

pattern(3)

#6. Write a python function which converts inches to cms.

def measure(inches):
    print("Cm: ",inches*2.54)

inches=int(input("Enter inches: "))
measure(inches)

#7. Write a python function to remove a given word from a list and strip it at the same time.

def rem(l,word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n

l=["harry", "mohit","shumbham","rohan","an"]
print(rem(l,"an"))

#8. Write a python function to print multiplication table of a given number

def table(n):
    for i in range(1,11):
        print(f"{n}X{i}={i*n}")
       
        
n=int(input("Enter No: "))
table(n)
