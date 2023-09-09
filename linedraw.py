import cv2 as cv
import numpy as np
img = np.zeros((513,512,3),np.uint8)
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img,(447,63),63,(0,0,255),-1)
ptd=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
ptd=ptd.reshape((-1,1,2))
cv.polylines(img,[ptd],True,(0,255,255))
font = cv.FONT_HERSHEY_DUPLEX
cv.putText(img,'BLAH',(10,500),font,4,(255,255,255),2,cv.LINE_AA)
cv.imshow('img',img)
cv.waitKey(0)==ord('q')
