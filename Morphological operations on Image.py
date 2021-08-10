import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread('smarties.png',0)
_, masked_img= cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal= np.ones((3,3), np.uint8)
dilation= cv2.dilate(src= masked_img, kernel=kernal, iterations=2)
erosion= cv2.erode(src=masked_img, kernel=kernal, iterations=2)
opening= cv2.morphologyEx(src= masked_img, op=cv2.MORPH_OPEN, kernel=kernal)
closing= cv2.morphologyEx(src= masked_img, op=cv2.MORPH_CLOSE, kernel=kernal)
gradient= cv2.morphologyEx(src= masked_img, op=cv2.MORPH_GRADIENT, kernel=kernal)
tophat= cv2.morphologyEx(src= masked_img, op=cv2.MORPH_TOPHAT, kernel=kernal)
blackhat= cv2.morphologyEx(src= masked_img, op=cv2.MORPH_BLACKHAT, kernel=kernal)

titles= ['smarties', 'masked img', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat', 'blackhat']
images= [img, masked_img, dilation, erosion, opening, closing, gradient, tophat, blackhat]

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()