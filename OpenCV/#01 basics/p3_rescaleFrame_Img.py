import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimenstion = (width,height)
    return cv.resize(frame,dimenstion,interpolation=cv.INTER_AREA)

img = cv.imread("images/airplan.jpeg")
resize_img = rescaleFrame(img,3)

cv.imshow('airplan',img) 
cv.imshow('airplan1',resize_img)
cv.waitKey(0)