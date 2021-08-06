import cv2

img= cv2.imread('messi5.jpg',1)

print(img.shape) #returns the tuple of number of rows,columns,and channels
print(img.size) #returns total number of pixels is accessed
print(img.dtype) #returns image datatype    

b,g,r= cv2.split(img)
img= cv2.merge((b,g,r))

#Grabbing the location of ball (our RoI) with mouse event:
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font= cv2.FONT_HERSHEY_COMPLEX
        line= cv2.LINE_AA
        strXY= str(x) + ', ' + str(y) 
        cv2.putText(img, strXY, (x, y), font, 0.5, (255,25,12), 1, line)
        cv2.imshow('image',img)

#Coping the ball(Region of Interest) part and placing it to other location:
ball= img[280:340,330:390]
img[273:333,100:160]= ball

cv2.imshow('image',img)

cv2.setMouseCallback('image', click_event)
cv2.imwrite('messi_ball.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
