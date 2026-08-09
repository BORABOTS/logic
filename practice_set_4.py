#1. Write a program to store seven fruits in a list entered by the user.

fruits= []
for i in range(0,7):
    f1=input("enter fruit name: ")
    fruits.append(f1)
print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
marks=[]

for i in range(0,6):
    a=int(input('enter marks: '))
    marks.append(a)
marks.sort()
print(marks)

#3. Check that a tuple type cannot be changed in python.
'''
a=(2,4,'lary')
a(2)="harry"
'''
#4. Write a program to sum a list with 4 numbers.

list1=[1,5,4,1]

print(sum(list1))

#a = (7, 0, 8, 0, 0, 9)
#5. Write a program to count the number of zeros in the following tuple
a=(7,0,8,0,0,9)
print(a.count(0))