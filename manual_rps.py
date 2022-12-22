import random
from random import choice
choices = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    print(f"The computer chose:{computer_choice}")
    return computer_choice

def get_user_choice():
    user_choice = input("Please enter your choice: ")
    print(f"{user_choice}")
    return user_choice


def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    elif (computer_choice == "Rock" and user_choice == "Paper") or \
         (computer_choice == "Paper" and user_choice == "Scissor") or \
         (computer_choice == "Scissor" and user_choice == "Rock"):
        #return user_choice
        print("You Won")
    else:
        print("You lost")

user_choice = get_user_choice()
computer_choice = get_computer_choice()
get_winner(computer_choice, user_choice)



