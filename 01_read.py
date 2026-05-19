import cv2

# Reading an Image

img = cv2.imread('media/image.png')
cv2.imshow('Output', img)
cv2.waitKey(0) # ~ ms

# Reading a Video

cap = cv2.VideoCapture('media/video.mp4')

while True:

    success, img = cap.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Reading the webcam

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 480)
cap.set(10, 100)

while True:

    success, img = cap.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break