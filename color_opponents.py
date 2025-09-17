#!/usr/bin/env python3

# import libraries
import cv2
import numpy as np


camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break


    mini = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    pad = np.zeros_like(mini)

    # create color channel images
    reds = np.zeros_like(mini)
    blues = np.zeros_like(mini)
    greens = np.zeros_like(mini)

    # red = mini[:,:,2]
    # blue = mini[:,:,0]
    # green = mini[:,:,1]

    reds[:,:,2] = mini[:,:,2]
    blues[:,:,0] = mini[:,:,0]
    greens[:,:,1] = mini[:,:,1]


    gray = cv2.cvtColor(mini, cv2.COLOR_BGR2GRAY)
    gray = np.stack((gray,)*3, axis=-1)

    # convert to L*a*b* color space, which emulates human opponent color processing
    cielab = cv2.cvtColor(mini, cv2.COLOR_BGR2Lab)
    L=128*np.ones_like(mini)
    a=128*np.ones_like(mini)
    b=128*np.ones_like(mini)
    L[:,:,0] = cielab[:,:,0]
    a[:,:,1] = cielab[:,:,1]
    b[:,:,2] = cielab[:,:,2]

    col0 = np.vstack((pad, mini, pad))
    col1 = np.vstack((reds, greens, blues))
    col2 = np.vstack((cv2.cvtColor(L, cv2.COLOR_Lab2BGR), cv2.cvtColor(a, cv2.COLOR_Lab2BGR), cv2.cvtColor(b, cv2.COLOR_Lab2BGR)))

    disp = np.hstack((col0,col1, col2))
    cv2.imshow('Video Feed', disp)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    

camera.release()
cv2.destroyAllWindows()
