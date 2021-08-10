import numpy as np
import cv2
import matplotlib.pyplot as plt

img1= cv2.imread('lena.jpg',1)
cv2.imshow('cv2 Image',img1)

#matplotlib read image in RGB formate. Hence, we have to convert BGR to RGB format.
img2=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

plt.imshow(img2)
#To remove xticks and yticks
#plt.xticks([])
#plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()