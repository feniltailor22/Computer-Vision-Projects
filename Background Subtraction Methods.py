import cv2
import numpy as np

cap=cv2.VideoCapture('vtest.avi')

#createBackgroundSubtractorMOG is a Gaussian Mixture-based Background/Foreground segmentation algorithm.
fgbg1= cv2.createBackgroundSubtractorMOG2()

#createBackgroundSubtractorKNN is a K-nearest neighbours-based Background/Foreground segmentation algorithm.
fgbg2= cv2.createBackgroundSubtractorKNN(detectShadows=False)

while True:
    ret, frame= cap.read()
    if frame is None:
        break

    #Applying background subtraction method on frame    
    fgmask1= fgbg1.apply(frame) 
    fgmask2= fgbg2.apply(frame)   

    cv2.imshow('Frame', frame)
    cv2.imshow('GMM FG Mask Frame', fgmask1)
    cv2.imshow('KNN FG Mask Frame', fgmask2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()