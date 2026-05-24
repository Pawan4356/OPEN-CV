import cv2

img = cv2.imread('../media/image.png')
print(img.shape)
cv2.imshow('Image', img)

img_resize = cv2.resize(img, (200, 500))
cv2.imshow('Resized Image', img_resize)

img_crop = img[:200, :200]
cv2.imshow('Croped Image', img_crop)

cv2.waitKey(0)