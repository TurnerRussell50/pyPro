import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)
pan=90
tilt=135
kit.servo[2].angle=pan
kit.servo[3].angle=tilt

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)

face_cascade=cv2.CascadeClassifier('/home/tom/Desktop/pyPro/cascade/face.xml')
eye_cascade=cv2.CascadeClassifier('/home/tom/Desktop/pyPro/cascade/eye.xml')

while True:
    ret, frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.7,9)
    for (x,y,w,h) in faces:
        Xcent=x+w/2
        Ycent=y+h/2
        errorPan=Xcent-dispW/2
        errorTilt=Ycent-dispH/2
        if (errorPan)>11:
            pan=pan-errorPan/30
        if (errorTilt)>11:
            tilt=tilt-errorTilt/30
        if (errorPan)<(-11):
            pan=pan+errorPan/30
        if (errorTilt)<(-11):
            tilt=tilt+errorTilt/30
        if pan>179:
            pan=179
            print('pan too bigly')
        if pan<1:
            pan=1
            print('pan too low')
        if tilt>179:
            tilt=179
            print('tilt too high dummy')
        if tilt<1:
            tilt=1
            print('tilt toolow dummy')

        kit.servo[2].angle=pan
        kit.servo[3].angle=tilt
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+h]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

        break

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows