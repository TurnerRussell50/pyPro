import cv2
print(cv2.__version__)
dispW=400
dispH=300
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
outVid=cv2.VideoWriter('videos/mycam.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH))

#cam2=cv2.VideoCapture(camSet2)
while True:
    ret, frame=cam.read()
 #   ret, frame2=cam2.read()
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanocam',0,0)
    outVid.write(frame)
    
  #  cv2.imshow('grayVideo',frame2)
   # cv2.moveWindow('grayVideo')
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
outVide.release()
cv2.DestroyAllWindows