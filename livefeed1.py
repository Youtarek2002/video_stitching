import cv2
import numpy as np

cam = cv2.VideoCapture(0)
fps=cam.get(cv2.CAP_PROP_FPS)
print(fps)
while True:
    success, frame = cam.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("cam",frame)
    cv2.waitKey(1)
    if not success:
        break;
