import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
def nothing(x):
    pass
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
cv2.namedWindow('nanoCam')
cv2.createTrackbar('xVal','nanoCam',25,dispW,nothing)
cv2.createTrackbar('yVal','nanoCam',25,dispH,nothing)
cv2.createTrackbar('rectWidth','nanoCam',25,dispW,nothing)
cv2.createTrackbar('rectHeight','nanoCam',25,dispH,nothing)
#cam2=cv2.VideoCapture(camSet2)
while True:
    ret, frame=cam.read()
 #   ret, frame2=cam2.read()
    xVal=cv2.getTrackbarPos('xVal','nanoCam',)
    yVal=cv2.getTrackbarPos('yVal','nanoCam',)
    rectWidth=cv2.getTrackbarPos('rectWidth','nanoCam',)
    rectHeight=cv2.getTrackbarPos('rectHeight','nanoCam',)
    cv2.rectangle(frame,(xVal,yVal),(xVal+rectWidth,yVal+rectHeight),(255,0,0),3)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    
  #  cv2.imshow('grayVideo',frame2)
   # cv2.moveWindow('grayVideo')
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.DestroyAllWindows