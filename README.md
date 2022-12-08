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

