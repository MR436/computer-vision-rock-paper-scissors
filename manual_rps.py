import random
from random import choice
list = ["rock", "paper", "scissors"]

def get_computer_choice():
    computer_choice = random.choice(list)
    print(f"The computer chose:{computer_choice}")

def get_user_choice():
    user_choice = input("Please enter your choice: ")
    print(f"{user_choice}")

def get_winner(computer_choice, user_choice):
    if computer_choice == "rock" and user_choice == "paper":
        return ("You won") 
    elif computer_choice == "paper" and user_choice == "scissor":
        return("You Won")
    elif computer_choice == "scissor" and user_choice == "rock":
        return("You Won")
    elif computer_choice == user_choice:
        return("Tie")
    else:
        return("You lost")


get_computer_choice()
get_user_choice()
get_winner()



