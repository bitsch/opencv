import numpy as np
import cv2


palm_cascade = cv2.CascadeClassifier('palm.xml')
fist_cascade = cv2.CascadeClassifier('.xml')
eye_cascade = cv2.CascadeClassifier('hand.xml')
cap = cv2.VideoCapture(0)
while( cap.isOpened() ) :
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fist = fist_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in fist:
    	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    palm = palm_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in palm:
    	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in eyes:
    	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('output',img) 
    k = cv2.waitKey(10)
    if k == 27:
        break

