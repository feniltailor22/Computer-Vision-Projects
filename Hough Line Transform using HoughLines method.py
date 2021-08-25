import numpy as np
import cv2

img= cv2.imread('sudoku.png')
gray_img= cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
edges= cv2.Canny(image=gray_img, threshold1=50, threshold2=150, apertureSize=3)
lines= cv2.HoughLines(image=edges, rho=1, theta=np.pi/180, threshold=200)

for line in lines:
    rho, theta= line[0]
    a= np.cos(theta)
    b= np.sin(theta)
    x0= a*rho
    y0= b*rho
    #x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1= int(x0 + 1000 * (-b))
    #y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
    y1= int(y0 + 1000 * (a))
    #x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
    x2= int(x0 - 1000 * (-b))
    #y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2= int(y0 - 1000 * (a))
    cv2.line(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0,0,255), thickness=2)

cv2.imshow('Edge',edges)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()