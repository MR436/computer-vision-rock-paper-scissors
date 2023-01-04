import cv2
from keras.models import load_model
import numpy as np
import random
import time
choices = ["Rock", "Paper", "Scissors"]
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
 
start_countdown = time.time()
end_countdown = time.time()
print(end_countdown - start_countdown)


def get_prediction():
	index = np.argmax(prediction, axis = 0)
	index = prediction[0][1]
print(index)
			
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    print(f"The computer chose:{computer_choice}")
    return computer_choice

def get_winner(computer_choice, get_prediction):
    if computer_choice == "Rock" and get_prediction == "Paper":
        #return user_choice
        print("You Won!")
    elif computer_choice == "Paper" and get_prediction == "Scissors":
        #return user_choice 
        print("You won!") 
    elif computer_choice == "Scissors" and get_prediction == "Rock":
        #return user_choice
        print("You won!") 
    elif computer_choice == get_prediction:
        print("It is a tie!")
    else:
        print("You lost")

get_prediction()
print(index)

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()