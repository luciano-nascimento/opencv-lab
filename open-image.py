import numpy as np
import cv2

img = cv2.imread("spitfire.png")
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

cv2.waitKey(0)

exit()
