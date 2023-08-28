import cv2 as cv

img = cv.imread("images/airplan.jpeg")
cv.imshow('airplan',img)

# converting to gray color
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('gray',gray)

# converting to another filter
filter = cv.cvtColor(img,cv.COLOR_RGB2LAB)
cv.imshow('filter',filter)
# blur
blur = cv.GaussianBlur(img, (0,0), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
# Edge cascode
canny = cv.Canny(img,100,200)
cv.imshow("Canny",canny)
#dilating the image
dilated = cv.dilate(canny,(3,3) ,iterations=2)
cv.imshow("dilated canny",dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations=2)
cv.imshow("Eroded",eroded)

#resize
resized = cv.resize(img,(img.shape[1]*3,img.shape[0]*3), interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resized)

# Cropping
cropped = img[50:200,200:300]
cv.imshow("cropped",cropped)

cv.waitKey(0)
