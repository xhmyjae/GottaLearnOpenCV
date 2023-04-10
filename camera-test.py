# How to use camera and apply a filter to the image

import numpy as np
import cv2

capDev = cv2.VideoCapture(0)

while True:
    ret, frame = capDev.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    cv2.imshow('frame2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
