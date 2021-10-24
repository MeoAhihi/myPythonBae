import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/trainner.yml')

id=0
#set text style
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (0,255,0)
fontcolor1 = (0,0,255)

def getProfile(id):
    conn=sqlite3.connect("FaceBaseNew.db")
    cursor=conn.execute("SELECT * FROM People WHERE ID="+str(id))
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

cam=cv2.VideoCapture(0);

while(True):
    ret,img=cam.read();
    img = cv2.flip(img, 1)

    centerH = img.shape[0] // 2;
    centerW = img.shape[1] // 2;
    sizeboxW = 300;
    sizeboxH = 400;
    cv2.rectangle(img, (centerW - sizeboxW // 2, centerH - sizeboxH // 2),
                  (centerW + sizeboxW // 2, centerH + sizeboxH // 2), (255, 255, 255), 5)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        id,dist=recognizer.predict(gray[y:y+h,x:x+w])
        profile = getProfile(id)

        #profile=None
        #if (dist<=25):
          #  profile=getProfile(id)

        if(profile!=None):
            cv2.putText(img, "Name: " + str(profile[1]), (x,y+h+30), fontface, fontscale, fontcolor ,2)
        else:
            cv2.putText(img, "Name: Unknown", (x, y + h + 30), fontface, fontscale, fontcolor1, 2)

    cv2.imshow('Face',img)
    if cv2.waitKey(1)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()

