import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size

img= cv2.imread('lena.jpg',1)
img= cv2.cvtColor(src= img, code=cv2.COLOR_BGR2RGB)

#Homogeneous Filter
kernel= np.ones((5,5), np.float32)/25
dst= cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

#Average filter/Low Pass Filter helps in removing noises, blurring the images.
blur= cv2.blur(src=img, ksize=(5,5))

#High Pass Filter helps in finding edges in the images.
gblur= cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0)

#Median filter is used to remove sal and paper noise from the image.
median= cv2.medianBlur(src=img, ksize=5)

#Bilateral filter remove noise while preserving border precisely. 
bilateral= cv2.bilateralFilter(src=img, d=9, sigmaColor=75, sigmaSpace=75)

titles= ['image', '2D Convolution', 'blur', 'gaussian blur', 'median', 'bilateral']
images= [img, dst, blur, gblur, median, bilateral]

for i in range(6):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()