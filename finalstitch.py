import cv2
import numpy as np
import imutils

cam1 = cv2.VideoCapture("campus12 (1) (online-video-cutter.com).mp4")
cam2 = cv2.VideoCapture("campus12 (1) (online-video-cutter.com) (1).mp4")
out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'XVID'),24,(800,650))
while True:
    success, frame1 = cam1.read()
    success1, frame2 = cam2.read()
    if not success or not success1:
        break;
    frame1 = cv2.flip(frame1, 1)
    frame2 = cv2.flip(frame2,1)
    images = []
    images.append(frame1)
    images.append(frame2)
    imagestitcher = cv2.Stitcher_create()
    error, stitched = imagestitcher.stitch(images)
    stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0, 0, 0))
    if len(stitched.shape) == 3 and stitched.shape[2] == 3:
      gray_stitched = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray_stitched, 0, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    area = max(contours, key=cv2.contourArea)
    mask = np.zeros(thresh.shape, dtype="uint8")
    x, y, w, h = cv2.boundingRect(area)
    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    minrec = mask.copy()
    sub = mask.copy()

    while cv2.countNonZero(sub) > 0:
        minrec = cv2.erode(minrec, None)
        sub = cv2.subtract(minrec, thresh)
    contours = cv2.findContours(minrec.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    area = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(area)
    stitched = stitched[y:y + h, x:x + w]
    if stitched is not None and len(stitched.shape)==3 :
        height,width,channels = stitched.shape
        if height>0 and width>0:
          stitched=cv2.resize(stitched,(800,650))
          cv2.imshow("stitched0", stitched)
          out.write(stitched)
          cv2.waitKey(1)
        else:
          continue


out.release()
cv2.destroyAllWindows()