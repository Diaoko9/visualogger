import numpy as np
import cv2 as cv
import tesserocr as tesser


#pipeline = 'device=/dev/video0 ! camera-id=0 ! video/x-h264, format=YUY2 ! videoconvert ! format=BGR ! appsink drop=1'
#pipeline = "device=/dev/video0 ! camera-id=0 ! autovideosink"

#cap = cv.VideoCapture(pipeline, cv.CAP_GSTREAMER)
cap = cv.VideoCapture(-1)
if not cap.isOpened():
    print("Cannot open Camera")
    exit()

while True:
 ret, frame = cap.read()

 if not ret:
    print("Cant recieve frame...")
    break



 gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

 cv.imshow('frame',gray)

 if cv.waitKey(1) == ord('q'):
    break

cap.release()
cv.destroyAllwindows()