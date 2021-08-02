import cv2

cap=cv2.VideoCapture(0);
#If we want to upload the video from computer:
#cap=cv2.VideoCapture('Video Path');

#Saving the captured video

fourcc= cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
#output.avi is output video file name.
#fourcc= 4-character code of codec used to compress the frames.
#frames per second=20
#framesize= (Height,Weight)= (640,480) 

print(cap.isOpened())

#Creating While loop to capture the frame continuosly

while (cap.isOpened()):
    ret, frame=cap.read()
    
    #Reading method gives True as an output if the cap(VideoCapture) is available and storing it as a frame.
    # ret= returning True or False 
    
    if ret == True:
    #If we want gray scale video capturing then use below command:
    #For color video capturing, we dont need it.
    #gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame',gray)

        #Printing height and width of the video frame:
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
   
        out.write(frame)

        cv2.imshow('frame',frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:       
        break

out.release()
cap.release()
cv2.destroyAllWindows()
    
#If video is on and we press 'q' key then all video frame will be distroyed.