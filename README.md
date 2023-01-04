# Computer Vision RPS

This project using Tensor flow which is python library is designed to make building neural networks for machine learning easy. 
The model has captured multiple images for paper, rock, scissors signes. These images were then used to train the model. 
The model trained is downloaded and added into the codes. Two important libraries numpy and keras were used for this program. 

"""Insert your code here"""
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Rock paper scissor is a game played using hand gestures to make these signs. The players say any of the word and form the hands into the shape of the word they choose. These rules apply and determine who wins the game: 
•	Rock smashes scissors.
•	Paper covers rock.
•	Scissors cut paper.

Before the code begins, we created a separate virtual environment in conda with command – conda create: 
   conda create -n my_env python=3.8
The environment name was: my_env and created using conda create command. 


Here we begin the code writing. Firstly we define the three options and store in a list: 
choices = ["Rock", "Paper", "Scissors"]
 
The main code starts here by creating two functions: 
•	user_choice
•	computer_choice

User_choice: This is very straight forward process. The task require to ask the choice from the user, as what action what would choose among: rock, paper, scissor. This input value is then assigned to the user_choice variable. The return function is called to get the input from user. Once user has given their input, another choice is required from the computer.
     user_choice = input("Please enter your choice: ")

Computer choice: This function is created for the purpose of automated selection of choice by the computer. The task is achieved by using random function. The randon method selects a choice for computer and return that choice.  The random.choice() is used for computer to randomly select between the actions:
    computer_choice = random.choice(choices)

<img width="417" alt="image" src="https://user-images.githubusercontent.com/110827214/210560154-2b890d85-57a0-4ff7-9ae8-3e5bf5daeade.png">


The main logic on which the game works is defined under get_winner function. The purpose of get_winner function is to let the code decide who wins the game and return the message to user, if they win or lost. This function takes two arguments: computer_choice and user_choice, which have been defined before. 

We use if-elif – else statement to define the logic how the game is played. Using if statement conditions, we compare user_choice and computer_choice to determine the winner. Based on the game conditions, if the computer chooses rock and the user chooses scissors, the computer wins. If the computer wins, the function should print "You lost", if the user wins, the function should print "You won!", and if it's a tie, the function should print "It is a tie!".

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock" and user_choice == "Paper":
        #return user_choice
        print("You Won!")
    elif computer_choice == "Paper" and user_choice == "Scissors":
        #return user_choice 
        print("You won!") 
    elif computer_choice == "Scissors" and user_choice == "Rock":
        #return user_choice
        print("You won!") 
    elif computer_choice == user_choice:
        print("It is a tie!")
    else:
        print("You lost")

Lastly, the play function is created where get_winner function is called to play the game and determine the winner. 


def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    get_winner(computer_choice, user_choice)

play()



