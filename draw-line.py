import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()
    #draw line
    #params: frame,two points x,y ,colors in rgb, thickness
    #line
    cv2.line(frame,(10,10),(500,10),(255,20,147),3)
    #rectangle
    cv2.rectangle(frame,(50,50),(250,200),(255,20,147),3)
    cv2.imshow('frame',frame)
    #press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
