import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue= img[y,x,0]
        green= img[y,x,1]
        red= img[y,x,2]
        cv2.circle(img, (x, y), 3, (0,0,255), -1)
        mycolorimage= np.zeros((512,512,3), np.uint8)
        
        mycolorimage[:]= [blue, green, red]
        
        cv2.imshow('color', mycolorimage)
    
img= cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
points= []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.imwrite('lena_mouse_events_3.0.jpg',img)
cv2.destroyAllWindows()