import random
def options():
    choices=["rock","paper","scissors"]
    return choices


def user_input(choices):
    while True:
        user_choice=input("Insert your choice.\n").lower()
        if user_choice not in choices:
            print("Invalid choice!")
        else:
            return user_choice
        
def computer_choice(choice):
    computer_choose=random.choice(choice)
    print(f"Robo chose {computer_choose}.")
    return computer_choose


def run_choice(computer_choose,user_choice):
    list_computer=[]
    list_user=[]
    win="You have won"
    comp_win="Robo won."
    if computer_choose=="paper" and user_choice == "scissor":
        print(win)
        list_computer.append(win)
    elif computer_choose =="scissor" and user_choice == "rock":
        print(win)
        list_computer.append(win)
    elif computer_choose== "rock" and  user_choice == "paper":
        print(win)
        list_computer.append(win)
    if user_choice=="paper" and computer_choose== "scissor":
        print(comp_win)
        list_computer.append(win)
    elif user_choice =="scissor" and computer_choose == "rock":
        print(comp_win)
        list_user=[]
    elif user_choice== "rock" and  computer_choose == "paper":
        print(comp_win)
        list_user=[]
    elif user_choice == computer_choose:
        print("Draw")
    print(list_user)
        
    
if __name__=="__main__":
    for i in range(3):
        choices=options()
        user_choice=user_input(choices)
        computer_choose =computer_choice(choices)
        run_choice(computer_choose,user_choice)
    