import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam2=cv2.VideoCapture(camSet2)

PL=cv2.imread('pl.jpg')
PL=cv2.resize(PL,(76,76))
cv2.imshow('LogoWindow',PL)
cv2.moveWindow('LogoWindow',850,0)

PLGray=cv2.cvtColor(PL,cv2.COLOR_BGR2GRAY)
cv2.imshow('LGGray',PLGray)
cv2.moveWindow('LGGray',850,140)

_,BGMask=cv2.threshold(PLGray,245,255,cv2.THRESH_BINARY)
cv2.imshow('BGMask',BGMask)
cv2.moveWindow('BGMask',850,250)

FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',850,360)

FG=cv2.bitwise_and(PL,PL,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',850,470)

BW=76
BH=76
Xpos=10
Ypos=10
dX=1
dY=1


while True:
    ret, frame=cam.read()
 #   ret, frame2=cam2.read()
    ROI=frame[Ypos:Ypos+BH,Xpos:Xpos+BW]
    ROIBG=cv2.bitwise_and(ROI,ROI,mask=BGMask)
    cv2.imshow('ROIBG',ROIBG)
    cv2.moveWindow('ROIBG',850,580)
    
    ROInew=cv2.add(FG,ROIBG)
    cv2.imshow('ROInew',ROInew)
    cv2.moveWindow('ROInew',850,690)

    frame[Ypos:Ypos+BH,Xpos:Xpos+BW,]=ROInew

    if Xpos<=0 or Xpos+BW>=dispW:
      dX=dX*(-1)
    if Ypos<=0 or Ypos+BH>=dispH:
      dY=dY*(-1)

    Xpos=Xpos+dX
    Ypos=Ypos+dY

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    
  #  cv2.imshow('grayVideo',frame2)
   # cv2.moveWindow('grayVideo')
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.DestroyAllWindows