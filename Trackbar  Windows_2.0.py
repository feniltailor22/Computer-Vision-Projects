import numpy as np
import cv2

cv2.namedWindow('image')

def nothing(x):
    print(x)

switch= 'color/gray'

#Creating Trackbar
cv2.createTrackbar('CP','image',10,400,nothing)
cv2.createTrackbar(switch,'image',0,1,nothing)

while(True):
    img= cv2.imread('lena.jpg')
    
    #Printing current position in the TrackBar
    pos= cv2.getTrackbarPos('CP','image')
    font= cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos), (50,150), font, 4, (0,0,255),10)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    s=cv2.getTrackbarPos(switch,'image')

    if s==0:
        pass
    else:
        img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    img= cv2.imshow('image',img)

cv2.destroyAllWindows()