import cv2 as cv

img = cv.imread("images/airplan.jpeg")
cv.imshow('airplan',img)

cv.waitKey(0)
