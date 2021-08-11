#Image Blending Method have five steps:
#(i) Load Two Images(same size) that you want to Blend.
#(ii) Find the Gaussian Pyramids for both of the Images.
#(iii) From Gaussian Pyramids, find their Laplacian Pyramids.
#(iv) Now join the left half og Image-1 and right half of Image-2 in each level of Laplacian Pyramids.
#(v) Finally from this joint image pyramids, reconstruct the original image.

import numpy as np
import cv2

apple= cv2.imread('apple.jpg',1)
orange= cv2.imread('orange copy.jpg',1)

print(apple.shape)
print(orange.shape)

#Half Apple and Half Orange in one Image without Blending
apple_orange= np.hstack((apple[:, :256],orange[:, 256:]))

#Generate Gaussian Pyramids for Apple
apple_layer= apple.copy()
gp_apple= [apple_layer]

for i in range(6):
    apple_layer= cv2.pyrDown(apple_layer)
    gp_apple.append(apple_layer)

#Generate Gaussian Pyramids for Orange
orange_layer= orange.copy()
gp_orange= [orange_layer]

for i in range(6):
    orange_layer= cv2.pyrDown(orange_layer)
    gp_orange.append(orange_layer)

#Generate Laplacian Pyramids for Apple
apple_layer= gp_apple[5]
lp_apple= [apple_layer]

for i in range(5, 0, -1):
    gaussian_extended_apple= cv2.pyrUp(gp_apple[i])
    laplacian= cv2.subtract(src1=gp_apple[i-1], src2=gaussian_extended_apple)
    lp_apple.append(laplacian)

#Generate Laplacian Pyramids for Orange
orange_layer= gp_orange[5]
lp_orange= [orange_layer]

for i in range(5, 0, -1):
    gaussian_extended_orange= cv2.pyrUp(gp_orange[i])
    laplacian= cv2.subtract(src1=gp_orange[i-1], src2=gaussian_extended_orange)
    lp_orange.append(laplacian)

#Now add left and right halves of images in each level
apple_orange_pyramid=[]
n=0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n+=1
    cols, rows, ch= apple_lap.shape
    laplacian= np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#Now reconstruct
apple_orange_reconstruct= apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct= cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct= cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('apple_orange',apple_orange)
cv2.imshow('apple_orange_reconstruct',apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()