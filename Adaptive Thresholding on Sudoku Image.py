#Adaptive Thresholding calculates thresholds for a smaller region of the Image. 
#Hence we get different thresholding values for different regions of the same image.
#It is useful in the images in which the lighting conditionds vary pixel to pixel.

import numpy as np
import cv2

img= cv2.imread('sudoku.png',0)

_, th1= cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

th2= cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11,C=2)
#cv2.ADAPTIVE_THRESH_MEAN_C method provides mean of the neighbourhood pixels(i.e. block size) as a threshold value.   
# C Constant subtracted from the mean.

th3= cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11,C=2)
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C method provides gaussian weighted sum of the neighbourhood pixels(i.e. block size) as a threshold value.
# C Constant subtracted from the sum.

cv2.imshow('Input Image',img)
cv2.imshow('Binary Thres',th1)
cv2.imshow('Adaptive Mean Thres',th2)
cv2.imshow('Adaptive Gaussian Thres',th3)

cv2.waitKey(0)
cv2.destroyAllWindows()