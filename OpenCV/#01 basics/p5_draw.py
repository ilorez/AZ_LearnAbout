import cv2 as cv
import numpy as np

#--- blue squer insid dark window or img
blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank',blank)
blank[200:300,300:400] = 255,0,0
# cv.imshow('blue',blank)
#--- img
img = cv.imread('images/airplan.jpeg')
# cv.imshow('airplan',img)

#create rectangle
cv.rectangle(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2), (0,255,0),thickness=1 )
#? note :'''negative thickness will fill the obj with the color color'''
#create circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(255,0,255),-1)
# create line
cv.line(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2), (255,255,255),thickness=1 )

# create image
cv.putText(blank,"Zobair",(100,100),cv.FONT_HERSHEY_TRIPLEX,1,(255,255,0),1)
# show finnl image
cv.imshow("draw",blank)
cv.waitKey(0)