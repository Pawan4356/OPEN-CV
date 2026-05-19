import cv2
import numpy as np

img = cv2.imread('cards.png')

width, height = 350, 200

points1 = np.float32([[460, 630], [960, 430], [640, 940], [1170, 740]])
points2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(points1, points2)
img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Image', img)
cv2.imshow('Warped Image', img_output)
cv2.waitKey(0)