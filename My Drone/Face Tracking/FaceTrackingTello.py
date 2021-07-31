from utlis import *
import cv2

w,h = 480,360
pid = [0.5, 0.5, 0]
pError = 0
startCounter = 0  #0 for flight, 1 for no flight

myDrone = initializeTello()

while True:

## Flight
    if startCounter == 0: 
        myDrone.takeoff()
        startCounter = 1

    ## Step 1
    img = telloGetFrame(myDrone, w, h)
    ## Step 2
    img, info = findFace(img)
    print(info[0][0])
    ## Step 3
    pError = trackFace(myDrone, info, w, pid, pError)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        myDrone.land()