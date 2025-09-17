#!/usr/bin/env python3

# import libraries
import cv2
import numpy as np
import pyautogui

camera = cv2.VideoCapture(0)
maxKernel=30

while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mini = cv2.resize(gray, (0,0), fx=0.5, fy=0.5)

    # get cursor position
    x, y = pyautogui.position()
    W,H = pyautogui.size()
    # print(f"Cursor position: ({x}, {y})")

    dx = int(np.floor(maxKernel*x/W))+1
    dy = int(np.floor(maxKernel*y/H))+1

    # make sure kernel sizes are odd
    dx += dx % 2 == 0   
    dy += dy % 2 == 0
    # print(f"dx: {dx}, dy: {dy}")

    gau1 = cv2.GaussianBlur(mini, (dx,dx), 0)
    gau2 = cv2.GaussianBlur(mini, (dy, dy), 0)
    dog = gau2-gau1

    cv2.putText(mini, f"dx: {dx}, dy: {dy}", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.putText(gau1, f"Gaussian Blur {dx}px", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.putText(gau2, f"Gaussian Blur {dy}px", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.putText(dog, "Difference of Gaussian", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    disp = np.vstack((np.hstack([mini,gau1]), np.hstack([gau2,dog])))
    cv2.imshow('Video Feed', disp)  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    

camera.release()
cv2.destroyAllWindows()
