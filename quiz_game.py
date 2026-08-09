print("welcome to my computer quiz!")
playing=input("Do you want to play? ")
if playing.lower()!="yes":
    quit()

print("okay let's play :) ")
score=0

answer= input("waht does CPU stand for? ")
if answer.lower() =="central processing unit":
    print("Correct!")
    score+=1
else:
    print("incorrect!")

answer= input("waht does GPU stand for? ")
if answer.lower() =="graphic processing unit":
    print("Correct!")
    score+=1
else:
    print("incorrect!")

answer= input("waht does RAM stand for? ")
if answer.lower() =="random access memory":
    print("Correct!")
    score+=1
else:
    print("incorrect!")

answer= input("waht does PS stand for? ")
if answer.lower() =="power supply":
    print("Correct!")
    score+=1
else:
    print("incorrect!")

print("you got " + str((score/4)*100)  + " %")


