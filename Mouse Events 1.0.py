import cv2

#Mouse events available in OpenCV:
#events= [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font= cv2.FONT_HERSHEY_COMPLEX
        line= cv2.LINE_AA
        strXY= str(x) + ', ' + str(y) 
        cv2.putText(img, strXY, (x, y), font, 0.5, (255,25,12), 1, line)
        cv2.imshow('image',img)
    
    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue= img[y,x,0]
        green= img[y,x,1]
        red= img[y,x,2]
        font= cv2.FONT_HERSHEY_COMPLEX
        line= cv2.LINE_AA
        strBGR= str(blue)+ ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0,255,220), 1, line)
        cv2.imshow('image',img)

img= cv2.imread('lena.jpg',1)
cv2.imshow('image',img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.imwrite('lena_mouse_events_1.0.jpg',img)

cv2.destroyAllWindows()