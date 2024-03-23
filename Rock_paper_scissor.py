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


def run_choice(computer_choose,user_choice):
  
    win="You have won"
    comp_win="Robo won."
    if user_choice == "quit":
        print("Goodbye")
        return True
    elif computer_choose=="paper" and user_choice == "scissor":
        print(win)
      
    elif computer_choose =="scissor" and user_choice == "rock":
        print(win)

    elif computer_choose== "rock" and  user_choice == "paper":
        print(win)
      
    if user_choice=="paper" and computer_choose== "scissor":
        print(comp_win)
      
    elif user_choice =="scissor" and computer_choose == "rock":
        print(comp_win)
      
    elif user_choice== "rock" and  computer_choose == "paper":
        print(comp_win)
 
    elif user_choice == computer_choose:
        print("Draw")
    return False

if __name__=="__main__":
    welcome()
    for i in range(3):
        choices=options()
        user_choice=user_input(choices)
        if user_choice == "quit":
            break  
        computer_choose =computer_choice()
        if run_choice(computer_choose,user_choice):
            break 
    print("Game is over.")