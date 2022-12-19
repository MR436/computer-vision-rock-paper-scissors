import random
from random import choice
list = ["rock", "paper", "scissors"]

def get_computer_choice():
    computer_choice = random.choice(list)
    print(f"The computer chose:{computer_choice}")

def get_user_choice():
    user_choice = input("Please enter your choice")
    print(f"{user_choice}")

get_computer_choice()
get_user_choice()



