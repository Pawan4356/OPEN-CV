import cv2
import numpy as np

cap = cv2.VideoCapture(0)
success, img = cap.read()
canvas = np.zeros_like(img)
xp, yp = 0, 0

def callback(temp):
    pass

def get_contours(img):

    global xp, yp
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:

        largest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest) > 200:
            x, y, w, h = cv2.boundingRect(largest)
            cx = x + w // 2
            cy = y + h // 2

            if xp == 0 and yp == 0:
                xp, yp = cx, cy

            cv2.line(canvas, (xp, yp), (cx, cy), (0, 255, 0), 5)
            xp, yp = cx, cy

cv2.namedWindow('TrackBars')

cv2.createTrackbar('Hue min', 'TrackBars', 35, 179, callback)
cv2.createTrackbar('Hue max', 'TrackBars', 77, 179, callback)
cv2.createTrackbar('Sat min', 'TrackBars', 83, 255, callback)
cv2.createTrackbar('Sat max', 'TrackBars', 232, 255, callback)
cv2.createTrackbar('Val min', 'TrackBars', 17, 255, callback)
cv2.createTrackbar('Val max', 'TrackBars', 148, 255, callback)

while True:

    success, img = cap.read()

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('Hue min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue max', 'TrackBars')

    s_min = cv2.getTrackbarPos('Sat min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat max', 'TrackBars')

    v_min = cv2.getTrackbarPos('Val min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val max', 'TrackBars')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(img_hsv, lower, upper)

    img_result = cv2.bitwise_and(img, img, mask=mask)

    get_contours(mask)

    img = cv2.add(img, canvas)

    cv2.imshow('Video', img)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()