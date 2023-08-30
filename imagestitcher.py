import cv2
import numpy as np
import imutils


img1=cv2.imread('photo1.png')
img2=cv2.imread('image2.png')
cv2.imshow("1",img1)
cv2.waitKey(0)
cv2.imshow("2",img2)
cv2.waitKey(0)
images=[]
images.append(img1)
images.append(img2)
imagestitcher = cv2.Stitcher_create()

error, stitched = imagestitcher.stitch(images)
if not error:
    cv2.imwrite("stitched.png",stitched)
    cv2.imshow("stitched",stitched)
    cv2.waitKey(0)

