
import cv2 as cv
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimenstion = (width,height)
    return cv.resize(frame,dimenstion,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('./videos/1.mp4')
while True:
    isTrue, frame = capture.read()
    frame = rescaleFrame(frame, .3)
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()


