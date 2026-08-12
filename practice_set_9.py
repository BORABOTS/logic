#1. Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
#contains the word ‘twinkleʼ.
f= open("poem.txt")
content = f.read()
if "twinkle" in content:
    print(" The word twinkle is present in file")
else:
    print(" The word twinkle is not  present in file")
f.close()

#2. The game() function in a program lets a user play a game and returns the score as an
#integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
#Hi-score. You need to write a program to update the Hi-score whenever the game()
#function breaks the Hi-score.
import random
def game():
    print("you are playing a game")
    score= random.randint(1,100)
    with open("hiscore.txt") as f:
        hiscore= f.read()
        if hiscore!="":
             hiscore= int(hiscore)
        else:
             hiscore=0

    print(f"your score {score}")
    if score> int(hiscore) :
        #write in file
        with open("hiscore.txt","w") as f:
                f.write(str(score))

    return score
game()
        

#3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
#files. Place these files in a folder for a 13-year-old.
def generate_tables(n):
    table=''
    for i in range(1,11):
        table += f"{n}X{i} = {n*i}\n"
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generate_tables(i)


#4. A file contains a word “Donkey” multiple times. You need to write a program which
#replaces this word with ##### by updating the same file.
word="donkey"
with open("file.txt","r") as f:
    content= f.read()
contentNew= content.replace(word,"######")

with open("file.txt","w") as f:
    f.write(contentNew)

#5. Repeat program 4 for a list of such words to be censored file.
words=["donkey","ganda","bad"]
with open("file.txt","r") as f:
    content= f.read()
for word in words:
    content= content.replace(word,"#"*len(word))

with open("file.txt","w") as f:
    f.write(content)

#6. Write a program to mine a log file and find out whether it contains ‘pythonʼ.
with open("log.txt","r")as f:
    content=f.read()
if"python" in content:
    print("Yes python is present in content. ")
else:
    print("No python is not present in content. ")

#7. Write a program to find out the line number where python is present from ques 6.



with open("log.txt") as f:
    lines=f.readlines()
lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Yes python is present in line: {lineno}. ")
        break
    lineno += 1

else:
    print("No python is not present. ")
    

#8. Write a program to make a copy of a text file “this.txt”.
with open("this.txt") as f:
    content= f.read()
with open("this_copy.txt","w") as f:
    f.write(content)

#9. Write a program to find out whether a file is identical and matches the content of another
with open("this.txt")as f:
    content1=f.read()
with open("this_copy.txt")as f:
    content2=f.read()
if content1==content2:
    print("yes the content is same in both files.")
else:
    print("no content is not simlar")

#10. Write a program to wipe out the content of a file using python.
with open("this.txt","w")as f:
    f.write("")

#11. Write a python program to rename a file to “renamed_by_python.txt”.

with open("old.txt")as f:
    content= f.read()
with open("this.txt","w")as f:
    f.write(content)