import cv2
print(cv2.__version__)
dispW=400
dispH=300
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam2=cv2.VideoCapture(camSet2)
while True:
    ret, frame=cam.read()
    frame=cv2.rectangle(frame,(140,100),(180,240),(0,255,0),(5))
    frame=cv2.circle(frame,(200,150),50,(0,0,255),(2))
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame,'1st frame',(50,50),fnt,1,(255,0,150),2)
    frame=cv2.line(frame, (10,10),(366,288),(0,0,0),4)
    frame=cv2.arrowedLine(frame,(10,270),(380,10),(255,255,255),1)
 #   ret, frame2=cam2.read()
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanocam',0,0)

    
  #  cv2.imshow('grayVideo',frame2)
   # cv2.moveWindow('grayVideo')
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.DestroyAllWindows