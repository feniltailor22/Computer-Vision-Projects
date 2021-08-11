#Canny Edge Detection Algorithm is composed of 5 Steps.
#(i) Apply Gaussian Filter to smooth the Image in order to remove the Noise.
#(ii) FInd the Intensity Gradient of the Image.
#(iii) Apply Non-Maximum Supression to get rid of spurious response to Edge Detection.
#(iv) Apply Double Threshold to determine potential Edges.
#(v) Track Edges by Hysteresis i.e. finalize the detection of the Edges by supressing all the other weak Edges. 

import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread('messi5.jpg',0)

canny= cv2.Canny(image=img, threshold1=100, threshold2=200)

titles= ['image', 'Canny']
images= [img, canny]

for i in range(2):
    plt.subplot(1,2,i+1) 
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()