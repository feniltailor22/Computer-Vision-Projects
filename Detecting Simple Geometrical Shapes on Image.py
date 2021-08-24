import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread('shapes.png',0)
_, thresh= cv2.threshold(src=img, thresh=240, maxval=255, type=cv2.THRESH_BINARY)
contours, _= cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx= cv2.approxPolyDP(curve=contour, epsilon=0.01*cv2.arcLength(contour, True), closed=True)
    #cv2.approxPolyDp detects the number of polygonal curves with precision.
    cv2.drawContours(image=img, contours=[approx], contourIdx=0, color=(0,0,0), thickness=5)
    #Printing out the shape
    x= approx.ravel()[0] #x-coordinate
    y= approx.ravel()[1] #y-coordinate
    if len(approx)== 3:
        cv2.putText(img=img, text='Triangle', org=(x, y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,0))
    elif len(approx)== 4:
        #Deciding whether the shape is square or rectangle
        x, y, w, h= cv2.boundingRect(approx)
        aspectRatio= float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img=img, text='Square', org=(x, y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,0))
        else:
            cv2.putText(img=img, text='Rectangle', org=(x, y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,0))    
    elif len(approx)== 5:
        cv2.putText(img=img, text='Pentagon', org=(x, y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,0))
    elif len(approx)== 6:
        cv2.putText(img=img, text='Hexagon', org=(x, y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,0))
    else:
        cv2.putText(img=img, text='Circle', org=(x, y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,0))

cv2.imshow('shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()