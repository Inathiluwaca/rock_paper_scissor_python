import random

def welcome():
    print("Welcome to the rock,paper scissors game. You have three tries.\nInsert quit if you want to end game.")

def options():
    choices=["rock","paper","scissor","quit"]
    return choices


def user_input(choices):
    while True:
        user_choice=input("Insert your choice.\n").lower()
        if user_choice not in choices:
            print("Invalid choice!")
        else:
            return user_choice
        
def computer_choice():
    computer_choose=["rock","paper","scissor"]
    computer_choose=random.choice(computer_choose)
    print(f"Robo chose {computer_choose}.")
    return computer_choose


def run_choice(computer_choose, user_choice, computer_score, user_score):
    win = "You have won"
    comp_win = "Robo won."
    
    if user_choice == "quit":
        print("Goodbye")
        return True
    elif computer_choose == "paper" and user_choice == "scissor":
        user_score += 1
        print(win)
        
    elif computer_choose == "scissor" and user_choice == "rock":
        user_score += 1
        print(win)

    elif computer_choose == "rock" and user_choice == "paper":
        user_score += 1
        print(win)
        
    elif user_choice == "paper" and computer_choose == "scissor":
        computer_score += 1
        print(comp_win)
        
    elif user_choice == "scissor" and computer_choose == "rock":
        computer_score += 1
        print(comp_win)
        
    elif user_choice == "rock" and computer_choose == "paper":
        computer_score += 1
        print(comp_win)
    
    elif user_choice == computer_choose:
        print("Draw")
    
    return computer_score, user_score

if __name__ == "__main__":
    welcome()
    computer_score = 0
    user_score = 0
    choices = options()
    for i in range(3):
        user_choice = user_input(choices)
        if user_choice == "quit":
            break
        
        computer_choose = computer_choice()
        computer_score, user_score = run_choice(computer_choose, user_choice, computer_score, user_score)
    
    
    print("User score:", user_score)
    print("Computer score:", computer_score)
    print("Game is over.")