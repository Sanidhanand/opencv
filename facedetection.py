import cv2 as cv
faceCascade=cv.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
path = 'photos/ZUCK.jpg'
img=cv.imread(path)
img2gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(img2gray,1.1,4)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0,),2)
   

cv.imshow('result',img)
cv.waitKey(0)