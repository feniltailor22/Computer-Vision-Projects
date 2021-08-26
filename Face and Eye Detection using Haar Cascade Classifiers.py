import cv2

#Define the classifier
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade= cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap= cv2.VideoCapture(0)

while cap.isOpened():
    _, img= cap.read()

    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #CascadeClassifier works only with gray scale images

    #Detect faces inside the image
    faces= face_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=4)
    #scaleFactor= Parameter specifying how much the image size is reduced at wach image scale.
    #minNeighbors= Parameter specifying how many neighbors each candidate rectangle should have to retain it.

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 3)
        RoI_gray= gray[y:y+h, x:x+w]
        RoI_color= img[y:y+h, x:x+w]    
        eyes= eye_cascade.detectMultiScale(RoI_gray)
        for (ex, ey, ew, eh) in eyes:    
            cv2.rectangle(RoI_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 3)

    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()