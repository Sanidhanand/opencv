import cv2 as cv 
import sys
print(cv.__version__)
img = cv.imread('photos/VanGogh-starry_night.jpg')
cv.imshow('starry', img)

k=cv.waitKey(0)
if k == ord('s'):
    cv.imwrite("VanGogh-starry_night.jpg",img)
