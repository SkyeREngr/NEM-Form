import cv2
import mediapipe as mp
import numpy as np
import time

# hand identification program, detects if a hand is displayed

#checking opencv and mediapipe version
#print("Your OpenCV version is: " + cv2.__version__)
#print("Your mediapipe version is: " + mp.__version__)

# assigning camera to variable
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(True,1, 1, 0.5, 0.5)

while True:
    # reads image from camera
    success, img = cap.read()
    # converts BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # processes results from camera
    results = hands.process(imgRGB)

    # results.multi_hand_landmarks is the hand data
    # if the camera is receiving hand data,
    if results.multi_hand_landmarks:
        print('Hand detected')
    else:
        print('Hand not detected')
    # print(results.multi_hand_landmarks)

    cv2.imshow("Image", img)
    cv2.waitKey(1)