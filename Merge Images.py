import numpy as np
import cv2

img1= cv2.imread('messi5.jpg',1)
img2= cv2.imread('opencv-logo.png',1)


img1= cv2.resize(img1,dsize=(512,512))
img2= cv2.resize(img2,dsize=(512,512))

merge_img= cv2.add(img1,img2);
weighted_img=cv2.addWeighted(img1,0.9,img2,0.1,0);

cv2.imshow('image',merge_img);
cv2.imshow('image_',weighted_img);

cv2.waitKey(0)
cv2.destroyAllWindows()