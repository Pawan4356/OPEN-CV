import cv2
import numpy as np

img = np.zeros((400, 400, 3), np.uint8)

cv2.line(img, (0, 0), (300, 300), (255, 255, 255), 3)
cv2.rectangle(img, (0, 0), (100, 100), (0, 255, 0), 2)
cv2.rectangle(img, (100, 100), (200, 200), (255, 255, 255), cv2.FILLED)
cv2.circle(img, (200, 200), 100, (255, 0, 0), cv2.FILLED)
cv2.putText(img, 'Hello', (150, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)

cv2.imshow('Image', img)
cv2.waitKey(0)