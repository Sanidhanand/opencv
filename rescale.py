import cv2 as cv


def rescaleimage(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)




img=cv.imread('photos/VanGogh-starry_night.jpg')

if img is None:
    print("not there lol")
    exit()
frame_resized=rescaleimage(frame=img)
cv.imshow('frame',img)
cv.imshow('pic',frame_resized)  
cv.waitKey(0)==ord('j')

cv.waitKey(0)