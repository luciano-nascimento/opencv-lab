import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

    # cap frame
    ret, frame = cap.read()

    # set gray to image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # set frame to window
    cv2.imshow('frame',frame)
    #press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
#release all
cap.release()
cv2.destroyAllWindows()
