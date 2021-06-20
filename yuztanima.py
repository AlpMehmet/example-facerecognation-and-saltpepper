
import cv2  
import numpy as np  
# path  
en_buyuk=0
nx,ny,nw,nh=(0,0,0,0)
path = r'yuz2.jpg'
yuz_cast=cv2.CascadeClassifier( "C:\\Users\\pc\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
goz_cast=cv2.CascadeClassifier( "C:\\Users\\pc\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")
# Reading an image in default mode 
image = cv2.imread(path,1) 
imageB = cv2.imread("crop.jpg",1)
kamera=cv2.VideoCapture(0)
font                   = cv2.FONT_HERSHEY_SIMPLEX

fontScale              = 2
fontColor              = (255,255,255)
lineType               = 1
def mse(image, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((image.astype("float") - imageB.astype("float")) ** 2)
    err /= float(image.shape[0] * image.shape[1])
    return err 
print(image.shape[1])  
while True:
    ret,kare=kamera.read()
    gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_cast.detectMultiScale(gri,1.1,7)
    gozle=goz_cast.detectMultiScale(gri,1.1,7)
    #print("fsfsfd:",yuzler.shape[0])
    
    for (nx,ny,nw,nh) in yuzler:
        
         cv2.rectangle(kare,(nx,ny),(nx+nw,ny+nh),(255,0,0),2)
         bottomLeftCornerOfText = (nx,ny-2)
         cv2.putText(kare,'Hello World!', bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
    for (x,y,w,h) in gozle:
        if(ny/2*nx<y*x):
            cv2.rectangle(kare,(x,y),(x+w,y+h),(0,255,0),2)
         
    cv2.imshow("resim",kare)
   
   # for (x,y,w,h) in yuzler:
    #    newimg = cv2.resize(image[y:y+h, x:x+w],(int(39),int(39)))
    #  a=mse(newimg,imageB)
     #   if(en_buyuk==0):
      #      en_buyuk=a
        
       # if(a<en_buyuk):
        #    en_buyuk=a
         #   nx,ny,nw,nh=(x,y,w,h)
        
        #x,y,w,h=yuzler[5]
#cv2.imwrite("crop.jpg",image[y:y+h, x:x+w])    
    #cv2.rectangle(image,(nx,ny),(nx+nw,ny+nh),(255,255,255),2)
    if(cv2.waitKey(25) & 0xFF ==ord('q')):
        break

# Window name in which image is displayed 


    
kamera.release()
# Using cv2.imshow() method  
# Displaying the image  



window_name = 'image'
#cv2.imshow(window_name, image)
cv2.waitKey()