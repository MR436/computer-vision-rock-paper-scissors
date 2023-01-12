import cv2
from keras.models import load_model
import numpy as np
import random
import time
choices = ["Rock", "Paper", "Scissors"]
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def main():
    round_played = 0

    while True: 

        timer = 5
        start_time = time.time()

        while timer > 0:

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            current_time = time.time()

            if current_time - start_time >=1:
                timer -= 1
                print(timer)
                start_time = current_time
        else:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            print(prediction)
            rounds_played = get_winner(prediction, round_played)
            
            print(round_played)
            if round_played == 5 or cv2.waitKey(1) & 0xFF == ord('q'):
                break     
 

def get_prediction(prediction):
    index = np.argmax(prediction[0])
    return index
    print(index)
			
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    print(f"The computer chose:{computer_choice}")
    return computer_choice

def get_winner(prediction, round_played):  
    computer_wins = 0
    user_wins = 0
    computer_choice = get_computer_choice()
    user_choice = get_prediction(prediction)
    if computer_choice == "Rock" and user_choice == 3 or \
        computer_choice == "Paper" and user_choice == 2 or \
        computer_choice == "Scissors" and user_choice == 1:
        #return get_prediction
        print("You Won!")
        user_wins += 1
       
    elif computer_choice == "Paper" and user_choice == 1 or \
        computer_choice == "Scissors" and user_choice == 3  or \
        computer_choice == "Rock" and user_choice == 2:
        #return get_prediction 
        print("Computer won!") 
        computer_wins += 1

    else:
        print("It is a tie!")
        computer_wins += 1
        user_wins += 1

    round_played += 1
   
    print(round_played)

    print(f'Computer: {computer_wins} - User: {user_wins}')
    return round_played
    # print()               

main()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

    