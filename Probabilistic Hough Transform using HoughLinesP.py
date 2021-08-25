import numpy as np
import cv2

img= cv2.imread('sudoku.png')
gray_img= cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
edges= cv2.Canny(image=gray_img, threshold1=50, threshold2=150, apertureSize=3)
lines= cv2.HoughLinesP(image=edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2= line[0]
    cv2.line(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0,255,0), thickness=2)

cv2.imshow('Edge',edges)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()