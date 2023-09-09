import cv2 as cv
import numpy as np 
img=cv.imread('photos/VanGogh-starry_night.jpg')
px=img[100,100]
print(px)
blue=img[100,100,0]
print(blue)
swirl=img[280:340,330:390]
img[273:333,100:160]=swirl
cv.imshow('sa',img)
cv.waitKey(0)==ord('k')