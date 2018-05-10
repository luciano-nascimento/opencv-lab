import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()
    #draw line
    #params: frame,two points x,y ,colors in rgb, thickness
    #horizontal
    cv2.line(frame,(10,10),(500,10),(185,128,41),3)
    cv2.line(frame,(10,150),(500,150),(185,128,41),3)  
    #vertical
    cv2.line(frame,(10,10),(10,150),(185,128,41),3)
    cv2.line(frame,(500,10),(500,150),(185,128,41),3)
    cv2.imshow('frame',frame)
    #press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
