import cv2 as cv
import numpy as np

# Load two images
img1 = cv.imread('photos/VanGogh-starry_night.jpg')
img2 = cv.imread('photos/star.png')

assert img1 is not None, "File 'VanGogh-starry_night.jpg' could not be read or does not exist"
assert img2 is not None, "File 'star.png' could not be read or does not exist"

# Create a ROI (region of interest)
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Convert logo image to grayscale and create a binary mask
img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2_gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Apply the mask to the ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# Take the region of logo from the logo image
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# Combine the foreground and background
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

# Display the resulting image
cv.imshow('Result', img1)
cv.waitKey(0)
cv.destroyAllWindows()
