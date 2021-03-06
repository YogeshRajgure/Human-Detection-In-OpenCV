import time

import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

## Histogram of oriented gradients detector
# HOG (Histogram of Oriented Gradients)

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def Detector(frame):
    ## Using Sliding window concept
    rects, weights = HOGCV.detectMultiScale(frame,
                                            winStride=(4,4),
                                            padding=(8,8),
                                            scale=1.03)
    #we are using multiscale, as it will help to detect multiple objects in a frame
    rects = np.array([[x, y, x+w, y+h] for (x,y,w,h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.50)
    # above method helps to avoid the rect if there is an overlap of more than 65%
    c=1

    for x, y, w, h in pick:
        cv2.rectangle(frame, (x,y), (w,h),(139,34,104),2)
        cv2.rectangle(frame, (x,y-20), (w,y),(139,34,104),-1)
        cv2.putText(frame, f'P{c}',(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255),2)
        c+=1
    print("reached here")
    cv2.putText(frame,
                f'Total Persons : {c - 1}',
                (20,450),
                cv2.FONT_HERSHEY_DUPLEX,
                0.8,
                (255,255,255),
                2)
    #cv2.imwrite('human_img_output.jpg',frame)
    cv2.imshow('output',frame)
    return frame





