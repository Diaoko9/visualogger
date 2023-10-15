import cv2 as cv
import numpy as np
import pytesseract as pytesseract

cap = cv.VideoCapture(2)
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

# Adding custom options
custom_config = r'--oem 3 --psm 6'
d = pytesseract.image_to_string(frame, config=custom_config)
print(d)