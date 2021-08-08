import numpy as np
import cv2

img= cv2.imread('gradient.png')
_, th1= cv2.threshold(src=img,thresh=127,maxval=255,type=cv2.THRESH_BINARY)
#Pixel Values <thres will be 0.

_, th2= cv2.threshold(src=img,thresh=127,maxval=255,type=cv2.THRESH_BINARY_INV)
#Inverse of cv2.THRESH_BINARY inj which Pixel Values >thres will be 0.

_, th3= cv2.threshold(src=img,thresh=127,maxval=255,type=cv2.THRESH_TRUNC)
#In cv2.THRESH_TRUNC the o/p >thres value pixels will remailn the same as thres value.
#i.e. if thres=127 then the pixel value >127 will be 127.

_, th4= cv2.threshold(src=img,thresh=127,maxval=255,type=cv2.THRESH_TOZERO)
#In cv2.THRESH_TOZERO the pixel values <thres will be zero after thresholding. 

_, th5= cv2.threshold(src=img,thresh=127,maxval=255,type=cv2.THRESH_TOZERO_INV)
#cv2.THRESH_TOZERO_INV is inverse of cv2.THRESH_TOZERO.

cv2.imshow('Input Image',img)
cv2.imshow('Binary Thres',th1)
cv2.imshow('Inv Binary Thres',th2)
cv2.imshow('Trunc Thres',th3)
cv2.imshow('Thres to Zero',th4)
cv2.imshow('Thres to Zero Inv',th5)

cv2.waitKey(0)
cv2.destroyAllWindows()