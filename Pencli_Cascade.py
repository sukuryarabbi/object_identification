import cv2

capture = cv2.VideoCapture(0)

mycascade = cv2.CascadeClassifier("Cascade/cascadePencil.xml")

font = cv2.FONT_HERSHEY_SIMPLEX

while True : 

    ret,frame = capture.read()
    frame = cv2.flip(frame , 1)

    gray = cv2.cvtColor(frame , cv2.COLOR_RGB2GRAY)

    faces = mycascade.detectMultiScale(gray , 1.3 ,4)

    for x,y,w,h in faces : 

        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) ,3)
        cv2.putText(frame , "kalem" , (x,y) , font , 1 , (0,255,0) , cv2.LINE_4)

    cv2.imshow("Dedektor",frame)

    kInp = cv2.waitKey(1)

    if(kInp == ord("q")) : 
        break

capture.release()
cv2.destroyAllWindows()
