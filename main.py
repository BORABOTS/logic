import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear()
    print("=" * 45)
    print("          BORABOTS - Logic Projects")
    print("=" * 45)
    print("1. Number Guessing Game")
    print("2. Rock Paper Scissors")
    print("3. Snake Water Gun")
    print("4. Quiz Game")
    print("5. Choose Your Own Adventure")
    print("6. Pig Game")
    print("7. Password Generator")
    print("8. Password Manager")
    print("0. Exit")
    print("=" * 45)

def run_project(choice):
    projects = {
        "1": "number_guess.py",
        "2": "rock_paper_scissor.py",
        "3": "snake_water_gun_challenge.py",
        "4": "quiz_game.py",
        "5": "choose_your_own_adventure.py",
        "6": "pig.py",
        "7": "pass_generator.py",
        "8": "password_manager.py"
    }

    if choice in projects:
        file = projects[choice]
        print(f"\nRunning {file}...\n")
        os.system(f"python {file}")
        input("\nPress Enter to return to menu...")
    else:
        print("Invalid choice!")

while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "0":
        print("Goodbye!")
        break
    else:
        run_project(choice)
