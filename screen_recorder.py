import numpy as np 
import pyautogui
import cv2 as cv

codec = cv.VideoWriter_fourcc(*"MPEG")
output = cv.VideoWriter("Recorded.mp4",codec,60,(1920,1080))

cv.namedWindow('Recording',cv.WINDOW_NORMAL)
cv.resizeWindow('Recording',450,270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    output.write(frame)
    cv.imshow('Recording',frame)
    
    if cv.waitKey(1) == ord('q'):
        break
output.release()
cv.destroyAllWindow()