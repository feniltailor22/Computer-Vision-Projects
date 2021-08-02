import cv2

img= cv2.imread('lena.jpg',1)

#Drawing straight line in an image:
img= cv2.line(img, pt1=(0,0), pt2=(255,255), color=(25,32,130), thickness=5)
#(0,0)= starting point
#(255,255)= ending point
#(B,G,R)= color value
#Line thickness= 5
#If we want to draw a line with customized color then use rgb color picker from google and use it in BGR format

#Drawing arrowed line in an image:
img= cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 5)

#Drawing rectangle in an image:
img= cv2.rectangle(img, pt1=(384,0), pt2=(510,128), color=(0,255,0), thickness=5)

#Drawing circle in an image:
img= cv2.circle(img, center=(280,125), radius=60, color=(0,0,255), thickness=5)

#Adding Text in an image:
img= cv2.putText(img, text='Lena', org=(10,500), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=4, lineType= cv2.LINE_AA, color=(255,255,255), thickness=5)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()