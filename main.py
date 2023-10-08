import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open Camera")
    exit()

while True:
    ret, frame = cap.read()

if not ret:
    break
    print("Cant recieve frame...")




gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

cv.imshow('frame',gray)

if cv.waitkey(1) == ord('q'):
    break

cap.release()
cv.destroyAllwindows()