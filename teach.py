import cv2
import numpy as np
# Constants for the crop size
xMin = 0
yMin = 0
xMax = 320
yMax = 320

cap = cv2.VideoCapture(0)
while( cap.isOpened() ) :
    ret,img = cap.read()
    edges = cv2.Canny(img,100,200)
    edges = edges[yMin:yMax,xMin:xMax] # this is all there is to cropping
    cv2.imshow('output',edges)

    k = cv2.waitKey(10)
    if k == 99:
        for i in range(0,100):
            ret,img = cap.read()
            edges = cv2.Canny(img,100,200)
            edges = edges[yMin:yMax,xMin:xMax] # this is all there is to cropping
            cv2.imshow('output',edges)
            cv2.imwrite('new/%d.jpg' % i,edges)
            
    k = cv2.waitKey(10)
    if k == 27:
        break
