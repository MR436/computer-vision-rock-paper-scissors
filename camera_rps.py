import cv2
from keras.models import load_model
import numpy as np
import random
import time
choices = ["Rock", "Paper", "Scissors"]
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

round_played = 1

def main():
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

        countdown_time = 1
        start_countdown = time.time()
        end_countdown = time.time()
        timer = (end_countdown - start_countdown)
        print(timer)
        if timer == 0:
            play()
        else:
            break

#play()


     #break
    #     break
    
        # countdown here: if timer is not run out
    # when timer = 0 -> get_winner()   

def get_prediction():
    index = np.argmax(prediction[0])
    print(index)
			
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    print(f"The computer chose:{computer_choice}")
    return computer_choice

def get_winner(computer_choice, get_prediction):  
    computer_wins = 0
    user_wins = 0
    if computer_choice == "Rock" and get_prediction == 3 or \
        computer_choice == "Paper" and get_prediction == 2 or \
        computer_choice == "Scissors" and get_prediction == 1:
        #return get_prediction
        print("You Won!")
        user_wins += 1
       
    elif computer_choice == "Paper" and get_prediction == 1 or \
        computer_choice == "Scissors" and get_prediction == 3  or \
        computer_choice == "Rock" and get_prediction == 2:
        #return get_prediction 
        print("Computer won!") 
        computer_wins += 1

    else:
        if computer_choice == get_prediction:
            print("It is a tie!")
            computer_wins += 1
            user_wins += 1

    print(f'Computer: {computer_wins} - User: {user_wins}')
    # print()


def play():
    while True:
        round_played <= 5
        round_played = round_played + 1
        user_choice = get_prediction()
        computer_choice = get_computer_choice()
        get_winner(computer_choice, user_choice)


                

#play()

# def countdown():
#     countdown_time = 5
#     start_countdown = time.time()
#     end_countdown = time.time()
#     timer = (end_countdown - start_countdown)
#     if timer <= countdown_time:
#         break

main()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

    