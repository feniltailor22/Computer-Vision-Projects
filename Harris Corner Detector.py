import numpy as np
import cv2


img= cv2.imread('left01.jpg')
cv2.imshow('img', img)

gray= cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

dst= cv2.cornerHarris(src=gray, blockSize=2, ksize=3, k=0.04)
#blocksize= 2*2 neighbourhood
#ksize= Aperture parameter of Sobel derivative used.
#k= Harris detector free parameter in the equation

dst= cv2.dilate(src=dst, kernel=None)

#Reverting back to the original image with optimal threshould value and marking all the detected corners with red color
img[dst > 0.01 * dst.max()] = [0,0,255]

cv2.imshow('dst', img)

cv2.waitKey(0)
cv2.destroyAllWindows()