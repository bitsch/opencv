import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while( cap.isOpened() ) :
    ret,img = cap.read()
    edges = cv2.Canny(img,100,200)
    cv2.imshow('output',edges)

    k = cv2.waitKey(10)
    if k == 99:
        for i in range(0,100):
            ret,img = cap.read()
            W,H = img.shape[::-1]
            edges = cv2.Canny(img,100,200)
            cv2.imshow('output',edges)
            template=cv2.imread('new/%d.jpg' % i,edges)
            w, h = template.shape[::-1]
            # All the 6 methods for comparison in a list
            methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
                    'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

            for meth in methods:
                img = img2.copy()
                method = eval(meth)

                # Apply template Matching
                res = cv2.matchTemplate(img,template,method)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
 
    

                if(W>bottom_right[0] and H>bottom_right[1] and top_left[0]>20 and top_left[1]>20):
                   print "yes"
                cv2.rectangle(img,top_left, bottom_right, 255, 2)
                plt.subplot(121),plt.imshow(res,cmap = 'gray')
                plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                plt.subplot(122),plt.imshow(img,cmap = 'gray')
                plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                plt.suptitle(meth)
                plt.show()

            
    k = cv2.waitKey(10)
    if k == 27:
        break





