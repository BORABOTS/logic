import random
def game(enter):
    choices=["s","w","g"]
    computer_choice= random.choice(choices)
    if computer_choice == enter:
        print(f"Computer_choice: {computer_choice}")
        print("Game draw!")
    else:
        if computer_choice=="w"and enter=="s":
            print(f"computer_choice: {computer_choice}")
            print("Snake wins!")

        elif computer_choice=="w" and enter=="g":
            print(f"computer_choice: {computer_choice}")
            print("Water Wins!") 

        elif computer_choice=="s" and enter=="g":
            print(f"computer_choice: {computer_choice}")
            print("Gun Wins!")  

        elif computer_choice=="s" and enter=="w":
            print(f"computer_choice: {computer_choice}")
            print("Snake wins!")

        elif computer_choice=="g" and enter=="s":
            print(f"computer_choice: {computer_choice}")
            print("Gun Wins!")  

        elif computer_choice=="g" and enter=="w":
            print(f"computer_choice: {computer_choice}")
            
            print("Water Wins!")
        else:
            print("what do you entered ?")
    
while True:

#wants to play 
    enter=input("\t\t(w,s,g) Whats your input : ").lower()
    if enter not in ["w","s","g"]:
        print("Warning")
        continue
    print(f"You choose : {enter}")
    game(enter)
            
    name=input("\t\tWants to play more than please press  (y/n)").lower()

    if(name=="n"):
        print("Thanks for playing!")
        break
    elif name=="y":
        continue
    else:
        print("Wrong input!")
        break
