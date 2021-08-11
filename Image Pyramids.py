#Pyramid representation is a type of multi-scale signal representation in which an Image is subject to repeated smoothing and subsampling.
#Two types: (i)Gaussian Pyramid (ii)Laplacian Pyramid.

import numpy as np
import cv2

img= cv2.imread('lena.jpg',1)
layer= img.copy()
gaussian_pyramid= [layer]

for i in range(6):
    layer= cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)
    cv2.imshow(str(i), layer)

#Laplacian Pyramids are formed using Gaussian Pyramid.
#A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid.
#Laplacian Pyramids are used in Blending and Reconstruction of Images. 

layer= gaussian_pyramid[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
laplacian_pyramid= [layer]

for i in range(5, 0, -1):
    gaussian_extended= cv2.pyrUp(gaussian_pyramid[i])
    laplacian= cv2.subtract(src1=gaussian_pyramid[i-1], src2=gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()