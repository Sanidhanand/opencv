import numpy as np
import cv2 as cv

def resized(frame,scale=.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cap = cv.VideoCapture('videos/dog.mp4')

if not cap.isOpened():
    print("Video not loaded")
    exit()

while True:
    ret, frame = cap.read()
   


    if not ret:
        print("UH OH! Failed to read frame.")
        break


    resized_frame = resized(frame=frame)
    cv.imshow("video",frame)
    cv.imshow("resized video",resized_frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
