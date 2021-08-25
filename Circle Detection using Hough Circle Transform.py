import cv2
import numpy as np

img= cv2.imread('smarties.png')
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray= cv2.medianBlur(src=gray, ksize=5)
circles= cv2.HoughCircles(image=gray, method=cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
detected_circles= np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :]:
    cv2.circle(img=img, center=(x, y), radius=r, color=(0,255,0), thickness=3)
    #drawing centre of the circle
    cv2.circle(img=img, center=(x, y), radius=2, color=(0,255,255), thickness=3)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
