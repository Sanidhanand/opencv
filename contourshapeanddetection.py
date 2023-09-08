import cv2 as cv
import numpy as np

def getcontour(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)

        if area > 100:  # Decreased the minimum area threshold
            cv.drawContours(imgcontour, cnt, -1, (255, 0, 0, 7))
            peri = cv.arcLength(cnt, True)
            print(peri)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            print(approx)
            objCorner = len(approx)
            x, y, width, height = cv.boundingRect(approx)

            if objCorner == 3:
                objtype = "Triangle"
            elif objCorner == 4:
                aspratio = width / float(height)
                if aspratio > 0.95 and aspratio < 1.05:
                    objtype = "Square"
                else:
                    objtype = "Rectangle"
            elif objCorner > 6:
                objtype = 'Circle'
            elif objCorner == 6:
                objtype = "Hexagon"
            else:
                objtype = "Unknown"  # Default value for objtype if not a triangle

            cv.rectangle(imgcontour, (x, y), (x + width, y + height), (0, 255, 0), 2)
            cv.putText(imgcontour, objtype, (x + int(width / 2) - 30, y + int(height / 2)),
                       cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)  # Adjusted the font size and color

path = 'photos/shapes.png'
img = cv.imread(path)
imgcontour = img.copy()
bgr2gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img2blur = cv.GaussianBlur(bgr2gray, (7, 7), 1)
imgcanny = cv.Canny(img2blur, 50, 50)
blank = np.zeros_like(img)
getcontour(imgcanny)
cv.imshow('img', img)
cv.imshow('bgr2gray', bgr2gray)
cv.imshow('canny', imgcanny)
cv.imshow('blank', blank)
cv.imshow('imgcontour', imgcontour)

cv.waitKey(0)
