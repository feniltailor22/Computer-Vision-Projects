import numpy as np
import cv2


img= cv2.imread('left01.jpg')
cv2.imshow('img', img)

gray= cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

corners= cv2.goodFeaturesToTrack(image=gray, maxCorners=50, qualityLevel=0.01, minDistance=10)
corners= np.uint0(corners)

#Drawing circles in each detected corners
for i in corners:
    x, y= i.ravel()
    cv2.circle(img=img,center=(x, y), radius=3, color=255, thickness=-1)

cv2.imshow('dst', img)

cv2.waitKey(0)
cv2.destroyAllWindows()