import cv2

img= cv2.imread('lena.jpg',0)
# IMREAD_UNCHANGED = -1,
# IMREAD_GRAYSCALE = 0,
# IMREAD_COLOR = 1

#Printing image in pixel values
print(img)

cv2.imshow('image', img)

#To capture the image for longer time, we use capture key argument.

k= cv2.waitKey(0)

#If we press Esc key(27) then we will not save the image or else saving the copy of img by pressing 's' key:
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.jpg',img)
    cv2.destroyAllWindows()