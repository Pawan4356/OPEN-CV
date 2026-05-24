import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 480)
cap.set(10, 100)

while True:

    success, img = cap.read()
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4 )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)

    cv2.imshow('Detected Face', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break