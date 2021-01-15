import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam2=cv2.VideoCapture(camSet2)
while True:
    ret, frame=cam.read()
    roi=frame[50:250,200:400]
    roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
     
#   ret, frame2=cam2.read()
    
    cv2.imshow('ROI',roi)
    cv2.imshow('nanoCam',frame)
    cv2.imshow('Gray',roiGray)
    cv2.moveWindow('nanoCam',0,0)
    cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('Gray',705,250)
    
  #  cv2.imshow('grayVideo',frame2)
   # cv2.moveWindow('grayVideo')
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.DestroyAllWindows