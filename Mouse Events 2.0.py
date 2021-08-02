import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0,0,255), -1)
        points.append((x, y))
        if len(points) >=2:
            cv2.line(img,points[-1], points[-2], (255,0,0), 1)
        cv2.imshow('image',img)
    
img= cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
points= []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.imwrite('lena_mouse_events_2.0.jpg',img)
cv2.destroyAllWindows()