import cv2

############# Tracker Types #############

# OLD
# tracker = cv2.legacy.TrackerBoosting_create()
# tracker = cv2.legacy.TrackerMIL_create()
# tracker = cv2.legacy.TrackerTLD_create()
# tracker = cv2.legacy.TrackerMedianFlow_create()
# tracker = cv2.legacy.TrackerMOSSE_create()

# NEWER
# tracker = cv2.legacy.TrackerKCF_create()
tracker = cv2.legacy.TrackerCSRT_create()

url = 'http://10.248.95.194:8080/video' # Using IP Webcam app on Android

cap = cv2.VideoCapture(url)
success, img = cap.read()
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', 600, 400)
b_box = cv2.selectROI('Video', img, False)
tracker.init(img, b_box)

def draw_box():
    x, y, w, h = int(b_box[0]), int(b_box[1]), int(b_box[2]), int(b_box[3])
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3, cv2.LINE_AA)
    cv2.putText(img, 'Tracking', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

while (cap.isOpened()):
    timer = cv2.getTickCount()
    success, img = cap.read()
    success, b_box = tracker.update(img)

    if success:
        draw_box()
    else:
        cv2.putText(img, 'Tracking Failure', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.resizeWindow('Video', 600, 400)
    cv2.imshow("Video", img)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cap.release()   
cv2.destroyAllWindows()