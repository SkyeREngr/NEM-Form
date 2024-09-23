import sys
import numpy as np
import cv2
import random


#SIMPLE IMAGE READING AND MANIPULATION FROM A SAVED IMAGE
# //-1 is color ignoring transpacency, 0 is grayscale, 1 is unchanged and values transparency
# img = cv2.imread('assets/pfp.png', -1)
# img = cv2.resize(img, (400, 350))

#REPLACING CERTAIN SECTIONS OF A PICTURE WITH OTHER PIXEL VALUES (PNG)
# // .shape is (rows, colums, channels)
# // img[x][y] = B G R (transpacency)
# for i in range(67):
#     for j in range(img.shape[1]):
#        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 0]

#WEBCAM CAPTURE
'''
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''

#WEBCAM CAPTURE AND DRAWING
'''
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # //Coordinate for drawing line in param 2 and 3
    img = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 5)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 5)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''

#CORNERS AND FINDING CORNERS
'''
img = cv2.imread('assets/pfp.png', -1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#//(source img, number of corners, minimum quality, minimum euclidean distance)
corners = cv2.goodFeaturesToTrack(gray, 40, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (0, 255, 0), -1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#TEMPLATE MATCHING IMAGES
img = cv2.imread('assets/soccer_practice.jpg', 0)
template = cv2.imread('assets/ball.png', 0)
h, w = template.shape

#//Change which method is being used to see which works best for our use case
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + w, location[1] + h)
    
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""
GIT STUFF:
To push changes to git/github:
0) git pull                             (Before working to update to current branch)
1) git add .                            (adds all files to commit list)
2) git commit -m "<message>"
2.5) git branch -vv                     (double check it is going to the right branch)
3) git push -u origin <branch>

"""
print("this is my main file!")
