import cv2
import time
import cvzone
import numpy as np
import handtrackmodule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)

detector = htm.HandDetect()

while True:
    # reads image from camera
    success, img = cap.read()
    img = detector.findhands(img)
    lmList = detector.findposition(img, draw= False)
    if len(lmList) != 0: # check to see if there is a hand present before printing
        print(lmList[4], lmList[8], lmList[12], lmList[16], lmList[20])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[12][1], lmList[12][2]
        x4, y4 = lmList[16][1], lmList[16][2]
        x5, y5 = lmList[20][1], lmList[20][2]

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x4, y4), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x5, y5), 15, (255, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(img, str("Gesture"), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)