#An Image Gradient is a directional change in the intensity or color in an Image. 
#It is used to detect the Edges in the Images.

import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread('sudoku.png',0)

#Laplacian Gradient
lap= cv2.Laplacian(src=img, ddepth=cv2.CV_64F, ksize=3)
#cv2.CV_64F supports the negative numbers of an image produced by Laplacian Gradient.
lap= np.uint8(np.abs(lap))

#SobelX (Order of derivative X)
SobelX= cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0)
SobelX= np.uint8(np.abs(SobelX))

#SobelY (Order of derivative X)
SobelY= cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1)
SobelY= np.uint8(np.abs(SobelY))

#Combining SobelX and SobelY
SobelComb= cv2.bitwise_or(src1=SobelX, src2=SobelY)


titles= ['image', 'Laplacian', 'SobelX', 'SobelY', 'Sobel Combined', 'Canny']
images= [img, lap, SobelX, SobelY, SobelComb]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()