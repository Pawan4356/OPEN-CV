import cv2
import numpy as np

def click_event(event, x, y, flags, params):
    '''
    flags and params are optional parameters which may be required for specific events. 
    For example, if you want to track the mouse movement, you can use the 
    EVENT_MOUSEMOVE event and pass the current mouse position as a parameter.
    '''

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)

img = cv2.imread('cards.png')

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600, 600)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)