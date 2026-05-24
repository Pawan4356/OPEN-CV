import cv2
import numpy as np

img = cv2.imread('../media/image.png')
kernel = np.ones((5, 5), np.uint8)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', img_gray)

img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
cv2.imshow('Blur Image', img_blur)

img_canny = cv2.Canny(img, 100, 100)
cv2.imshow('Edges', img_canny)

img_dialation = cv2.dilate(img_canny, kernel, iterations=5)
cv2.imshow('Dialation', img_dialation)

img_erode = cv2.erode(img_dialation, kernel, iterations=3)
cv2.imshow('Erode', img_erode)

cv2.waitKey(0)