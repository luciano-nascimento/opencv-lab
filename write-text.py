import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()
    font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(frame,'hello world !',(30,30),font,1,(255,105,180),2)
    cv2.imshow('frame',frame)
    #press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
