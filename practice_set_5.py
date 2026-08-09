#1. Write a program to create a dictionary of Hindi words with values as their English
#translation. Provide user with an option to look it up!
words= {
    "billi":"cat",
    "kutta":"dog",
    "kursi":"chair"
}
word=input("enter the word: ")
print(words[word])


#2. Write a program to input eight numbers from the user and display all the unique numbers(once).
num=set()
for i in range(0,8):
    a=int(input('enter no: '))
    num.add(a)
print(num)

#3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s=set()
s.add(18)
s.add("18")
print("\n",s)


#4. What will be the length of following set s:
#s = set()
#s.add(20)
#s.add(20.0)
#s.add('20') # length of s after these operations?
s = set()
s.add(20)
s.add(20.0)#this is same as 20
s.add('20') 
print(len(s))

#5. 
#s = {}
#What is the type of 's'?
s={}
print(type(s))

#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
#use key as their names. Assume that the names are unique.
d={}
for i in range(0,4):
    name= input("enter friend name: ")
    lang= input("enter language name: ")
    d.update({name:lang})
print(d)


#7. If the names of 2 friends are same; what will happen to the program in problem 6?

d={}
for i in range(0,2):
    name= input('enter name: ')
    lang= input('enter language: ')
    d.update({name:lang})#the update method will update the value of last name
print(d)

#8. If languages of two friends are same; what will happen to the program in problem 6?
d={}
for i in range(0,2):
    name= input('enter name: ')
    lang= input('enter language: ')
    d.update({name:lang})# it is the language or value for another key
print(d)

#9. Can you change the values inside a list which is contained in set S?
#s = {8, 7, 12, "Harry", [1,2]}
s = {8, 7, 12, "Harry", [1,2]}
# element in set are all immutable and hasable
