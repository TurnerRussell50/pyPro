import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam1=cv2.VideoCapture(cv2.sensor_id[0])
cam2=cv2.VideoCapture(cv2.sensor_id[1])
while True:
    ret, frame=cam1.read()
    ret, frame=cam2.read()
    cv2.imshow('Cam1',frame)
    cv2.imshow('Cam2',frame2)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.DestroyAllWindows