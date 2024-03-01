import random
def user_input():
    choices=["rock","paper","scissors"]
    while True:
        user=input("Insert your choice.\n")
        if user not in choices:
            print("Invalid choice!")
        else:
            return choices


if __name__=="__main__":
    user_input()