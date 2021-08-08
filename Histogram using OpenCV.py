import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread('lena.jpg',0)

#Creating a mask
mask= np.zeros(img.shape, np.uint8)
mask[100:400, 100:400]= 255

masked_img= cv2.bitwise_and(img, img, mask= mask)

#Calculate histogram with mask and without mask
hist_img= cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
hist_masked_img= cv2.calcHist(images=[masked_img], channels=[0], mask=mask, histSize=[256], ranges=[0,256])

plt.subplot(3,2,1), plt.imshow(img,'gray')
plt.subplot(3,2,2), plt.imshow(mask, 'gray')
plt.subplot(3,2,3), plt.imshow(masked_img, 'gray')
plt.subplot(3,2,4), plt.plot(hist_img)
plt.subplot(3,2,5), plt.plot(hist_masked_img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()