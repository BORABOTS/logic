#1. Write a program to find the greatest of four numbers entered by the user.
a=int(input('enter number of a: '))
b=int(input('enter number of b: '))
c=int(input('enter number of c: '))
d=int(input('enter number of d: '))

greatest=max(a,b,c,d)
print("Greatest no of all four inputs: ",greatest)

#2. Write a program to find out whether a student has passed or failed if it requires a total of
#40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
#input from the user.
marks1 = int(input('enter marks: '))
marks2 = int(input('enter marks: '))
marks3 = int(input('enter marks: '))
total = marks1+ marks2+ marks3

percentage=(total/300)*100
if percentage >=40 and marks1 >=33 and marks2 >= 33 and marks3 >=33:
    print("student passed!")
    print("total: ",total)
    print("percentage: ",percentage)
else:
    print("student failed!")

#3. A spam comment is defined as a text containing following keywords: “Make a lot of
#money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

comment= input('enter your comment: ')
spam_words = [
    "make a lot of money",
    "buy now",
    "subscribe this",
    "click this"
]

if any(word in comment.lower() for word in spam_words):
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")

#4. Write a program to find whether a given username contains less than 10 characters or not.

name= input("enter username: ")
a=len(name)
if a>=10:
    print("Username contain 10 character.")
else:
    print("Username do not contain 10 char.")

#5. Write a program which finds out whether a given name is present in a list or not.

list1=["mohit","kunal","karan","abhay","nikhil"]
a=input("enter name: ")
if a in list1:
    print("The name is in the list: ",a)
else:
    print("NO such name.")


#6. Write a program to calculate the grade of a student from his marks from the following
#scheme:
#90 – 100 => Ex
#80 – 90 => A
#70 – 80 => B
#60 – 70 => C
#50 – 60 => D
#<50 => F
marks= int(input("enter marks: "))
if marks>=90 and 100<=marks:
    print("Grade Ex")
elif marks>=80 and 90<=marks:
    print("Grade A")
elif marks>=70 and 80<=marks:
    print("Grade B")
elif marks>=60 and 70<=marks:
    print("Grade C")
elif marks>=50 and 60<=marks:
    print("Grade D")
else:
    print("F-> fail")

#7. Write a program to find out whether a given post is talking about “Harry” or not.
post= input("enter your post: ")

if "harry" in post:
    print("They are talking about you!")
else:
    print("They are not talking about you!")
