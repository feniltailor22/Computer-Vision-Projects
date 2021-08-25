import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread('lena.jpg',1)
b, g, r= cv2.split(img)

cv2.imshow('img',img)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)

plt.hist(b.ravel(), bins=256, range=[0,256])
plt.hist(g.ravel(), bins=256, range=[0,256])
plt.hist(r.ravel(), bins=256, range=[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()