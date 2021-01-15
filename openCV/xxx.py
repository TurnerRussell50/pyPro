import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
dispW=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
BW=int(.15*dispW)
BH=int(.15*dispH)
posX=10
posY=10
dx=2
dy=2

#cam2=cv2.VideoCapture(camSet2)
while True:
    ret, frame=cam.read()
    roi=frame[0:640,0:480]
    roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    #ret, frame2=cam2.read()
    
    #cv2.imshow('ROI',roi)
    
    #cv2.imshow('Gray',roiGray)
    if posX<=0 or posX+BW>=dispW:
        dx=dx*(-1)
    if posY<=0 or posY+BH>=dispH:
        dy=dy*(-1)
    
    roiFrame=cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(0,0,0),1)
    roiColor=roiFrame
    cv2.imshow('nanoCam',roiColor)
    posX=posX+dx
    posY=posY+dy
    cv2.imshow('nanoCam',(roiGray)
    
    #cv2.imshow('grayVideo',frame2)
   # cv2.moveWindow('grayVideo')
    #if cv2.waitKey(1)==ord('q'):
     #   break

cam.release()
cv2.DestroyAllWindows