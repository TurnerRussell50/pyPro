import cv2
print(cv2.__version__)
evt=-1
coord=[]
def click(event,x,y,flags,params):
    global pnt
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse event was:     ',event)
        print(x,',',y)
        pnt=(x,y)
        coord.append(pnt)
        print(coord)
        evt=event
dispW=640
dispH=480
flip=2
cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam',click)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam2=cv2.VideoCapture(camSet2)
while True:
    ret, frame=cam.read()
    for pnts in coord:
            cv2.circle(frame,pnts,5(0,0,255),-1)
#   ret, frame2=cam2.read()

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanocam',0,0)

    
  #  cv2.imshow('grayVideo',frame2)
   # cv2.moveWindow('grayVideo')
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.DestroyAllWindows