import numpy as np
import cv2 as cv 

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Captures frame by frame
    ret, frame = cap.read()

    if not ret:
        # Handle the case when frame capture is unsuccessful
        print("Uh oh! Failed to capture frame.")
        break

    # Operations on the frame go here 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the frame
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
