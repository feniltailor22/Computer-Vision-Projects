import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape

img= cv2.imread('road.jpg')
img= cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)

print(img.shape)
height= img.shape[0]
width= img.shape[1]

#Defining RoI
region_of_interest_vertices= [
    (200,height),
    (814, 400),
    (width,height)
]

#Creating a function to mask the region other than RoI
def region_of_interest(img, vertices):
    mask= np.zeros_like(img)
    #Fill inside the polygon
    cv2.fillPoly(img=mask, pts=vertices, color=255)
    #Return the image only where the mask pixel matches
    masked_image= cv2.bitwise_and(img, mask)
    return masked_image

gray_img= cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
canny_image= cv2.Canny(image=gray_img, threshold1=100, threshold2=200)

cropped_image= region_of_interest(canny_image, 
                np.array(object=[region_of_interest_vertices], dtype=np.int32))

lines= cv2.HoughLinesP(image=cropped_image, rho=6, theta=np.pi/180, threshold=160, minLineLength=40, maxLineGap=25)

def draw_the_lines(img, lines):
    img= np.copy(img)
    blank_img= np.zeros(shape=(img.shape[0], img.shape[1], 3), dtype=np.uint8)
   
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img=blank_img, pt1=(x1, y1), pt2=(x2, y2), color=(0,255,0), thickness=3)
    
    #Merge the image with the lines into the original image
    img= cv2.addWeighted(src1=img, alpha=0.8, src2=blank_img, beta=1, gamma=0.0)
    return img

image_with_lines= draw_the_lines(img, lines)

plt.imshow(image_with_lines)
plt.show()