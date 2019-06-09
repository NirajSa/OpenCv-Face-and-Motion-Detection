import cv2

fc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

#img = cv2.imread("a.jpg")

#gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#faces = fc.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors = 5)

#for x,y,w,h in faces:
#    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

#print(type(faces))
#print(faces)

#cv2.imshow("Gray",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


while True:
    ret, img = video.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray)

    for (x,y,w, h) in faces:
        cv2.rectangle (img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #eyes eye cascade detectMultiScale (roi gray)
        #for (ex, ey, ew, eh) in eyes:
            #cv2.rectangle (roi_color, (ex, ey), (extew,ey+eh), (0,255,0), 2)

    cv2.imshow ('img',img)
    k = cv2.waitKey (30) & 0xff
    if k==27:
        break

cv2.release()
cv2.destroyAllWindows()
