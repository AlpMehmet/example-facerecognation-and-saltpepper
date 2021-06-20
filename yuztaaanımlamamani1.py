
import cv2  
import numpy as np  
# path  
en_buyuk=0
nx,ny,nw,nh=(0,0,0,0)
path = r'yuz2.jpg'
yuz_cast=cv2.CascadeClassifier( "C:\\Users\\pc\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
goz_cast=cv2.CascadeClassifier( "C:\\Users\\pc\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")
image = cv2.imread(path,1) 
imageB = cv2.imread("crop.jpg",1)
kamera=cv2.VideoCapture(0)
font                   = cv2.FONT_HERSHEY_SIMPLEX

fontScale              = 2
fontColor              = (255,255,255)
lineType               = 1
print(image.shape[1])  

while True:
    ret,kare=kamera.read()
    gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_cast.detectMultiScale(gri,1.1,7)
    gozle=goz_cast.detectMultiScale(gri,1.1,7)
    for (nx,ny,nw,nh) in yuzler:
         cv2.rectangle(kare,(nx,ny),(nx+nw,ny+nh),(255,0,0),2)
    for (x,y,w,h) in gozle:
        if(ny/2*nx<y*x):
            cv2.rectangle(kare,(x,y),(x+w,y+h),(0,255,0),2)
         
    cv2.imshow("resim",kare)
    if(cv2.waitKey(25) & 0xFF ==ord('q')):
        break
kamera.release()
window_name = 'image'
cv2.waitKey()