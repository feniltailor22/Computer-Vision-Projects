import cv2
import datetime

cap=cv2.VideoCapture(0);
#If we want to upload the video from computer:
#cap=cv2.VideoCapture('Video Path');

#Printing height and width of the video frame:
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Creating While loop to capture the frame continuosly

while (cap.isOpened()):
    ret, frame=cap.read()
    #Reading method gives True as an output if the cap(VideoCapture) is available and storing it as a frame.
    # ret= returning True or False 
    
    if ret == True:
        
        datet= str(datetime.datetime.now())
        font=cv2.FONT_HERSHEY_COMPLEX
        line= cv2.LINE_AA
        frame= cv2.putText(img=frame, text=datet, org=(10,50), fontFace=font, fontScale=1, color=(0,255,255), thickness=2, lineType=line)
        
        cv2.imshow('frame',frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:       
        break

cap.release()
cv2.destroyAllWindows()
    
#If video frame is on and we press 'q' key then all video frame will be distroyed.