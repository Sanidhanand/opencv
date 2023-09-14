import cv2 as cv
import numpy as np
img=cv.imread('photos/VanGogh-starry_night.jpg')
cv.imshow('img',img)
#blurry
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

cv.waitKey(0)==ord('j')