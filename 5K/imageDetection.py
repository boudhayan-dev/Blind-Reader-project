from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2,time
import numpy as np



def imageSubtract(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret,thresh = cv2.threshold(blur,65,255,cv2.THRESH_BINARY_INV)
    return thresh

camera = PiCamera()
camera.resolution = (512, 512)
camera.framerate = 30
camera.flash_mode='off'
rawCapture = PiRGBArray(camera, size=(512, 512))
rawCapture.truncate(0)
refImg=""
first_time=0
first_10_frame=0
counter=0
contour_area=[0,0]

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    rawCapture.truncate(0)
    if first_time==0:
        if first_10_frame<60:
            first_10_frame+=1
            continue
        time.sleep(2)
        refImg_color=frame.array
        refImg=cv2.cvtColor(refImg_color,cv2.COLOR_BGR2GRAY)
        refThresh=imageSubtract(refImg)
        first_time=1
        continue

    cv2.imshow("Ref Image",refImg_color)

    image = frame.array
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("NewImage", image)
    key = cv2.waitKey(1)

    

    newThresh=imageSubtract(gray)
    diff=cv2.absdiff(refThresh,newThresh)
    diff=cv2.bitwise_xor(diff,refThresh)
    kernel = np.ones((3,3),np.uint8)
    diff=cv2.erode(diff,kernel,iterations = 4)
    diff=cv2.dilate(diff,kernel,iterations = 2)
    cv2.imshow("Diff Image",diff)
    

    try:
    
        _, contours, _= cv2.findContours(diff,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        c=max(contours,key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(diff,(x,y),(x+w,y+h),(125,125,125),2)
        if cv2.contourArea(c)>500:
            if counter==0:
                print("Object entering frame . Going into sleep for 2 sec and resuming")
                time.sleep(2)
                counter=1
                continue
        if counter==1 :
            print("Object Area =",cv2.contourArea(c))
            print("Turning  the page to read the next page . . .")
            counter=0
            
               
    except Exception as e:
        #print(e)
        pass
    
    if key == 27:
        camera.close()
        cv2.destroyAllWindows()
        break











    
'''
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (512, 512)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')
'''
