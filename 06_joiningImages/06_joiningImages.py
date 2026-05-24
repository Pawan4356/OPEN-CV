import cv2
import numpy as np

img = cv2.imread('media/image.png')

# They need to have same number of channels -> You can use your own code to solve that...
img_hor = np.hstack((img, img))
img_ver = np.vstack((img, img))

cv2.imshow('Horizontal', img_hor)
cv2.imshow('Vertical', img_ver)

cv2.waitKey(0)