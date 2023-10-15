import numpy as np
import cv2 as cv

from pytesseract import pytesseract


#pipeline = 'device=/dev/video0 ! camera-id=0 ! video/x-h264, format=YUY2 ! videoconvert ! format=BGR ! appsink drop=1'
#pipeline = "device=/dev/video0 ! camera-id=0 ! autovideosink"

#cap = cv.VideoCapture(pipeline, cv.CAP_GSTREAMER)
cap = cv.VideoCapture(-1)
if not cap.isOpened():
    print("Cannot open Camera")
    exit()

counter = 0

while True:
 ret, frame = cap.read()
 counter+=1

 if ((counter%20)==0):
        
    imgH, imgW,_ = frame.shape
        
    x1,y1,w1,h1 = 0,0,imgH,imgW
        
    imgchar = pytesseract.image_to_string(frame)
        
    imgboxes = pytesseract.image_to_boxes(frame)
        
    for boxes in imgboxes.splitlines():
        boxes = boxes.split(' ')
        x,y,w,h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
        cv.rectangle(frame, (x, imgH-y), (w,imgH-h), (0,0,255),3)
            
        cv.putText(frame, imgchar, (x1 + int(w1/50), y1 + int(h1/50)), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        
        font = cv.FONT_HERSHEY_SIMPLEX

 #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

 


 cv.imshow('frame',frame)

 if cv.waitKey(1) == ord('q'):
    break

cap.release()
cv.destroyAllwindows()