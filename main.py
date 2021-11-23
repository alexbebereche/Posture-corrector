import cv2
import winsound

"""
TODO: debug multiple key presses needed for the instruction to function
"""

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

print("Press 'p' when you want to set a threshold")
RED = (0, 0, 255)
BLUE = (255, 0, 0)

IS_STRAIGHT = False
X_ = -1
Y_ = -1
MIN_FACE_HEIGHT = 170
TRIGGER = False

while True:
    ret, frame = cap.read()
    WIDTH = int(cap.get(3))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    
    for (x, y, w, h) in faces:
        if w < MIN_FACE_HEIGHT:
            break

        if IS_STRAIGHT == False:
            cv2.line(frame, (0, y - 5), (WIDTH, y - 5), (0, 255, 0), 2)
            X_ = (0, y - 5)
            Y_ = (WIDTH, y - 5)
            

        
        if y > Y_[1]:
            cv2.rectangle(frame, (x, y), (x + w, y + h), RED, 5)
            if TRIGGER == True:
                winsound.Beep(440, 500)
        else:    
            cv2.rectangle(frame, (x, y), (x + w, y + h), BLUE, 5)                                                                                                                   

    if IS_STRAIGHT == True:
        cv2.line(frame, X_, Y_, (0, 255, 0), 2)


    key = cv2.waitKey(1)
    if key == ord('p'):
        IS_STRAIGHT = True
        TRIGGER = True
        
        print("Selected threshold")

    elif key == ord('r'):
        IS_STRAIGHT = False
        TRIGGER = False

        print("Restarted threshold. Select another one")
    elif cv2.waitKey(1) == ord('q'):
        break

    cv2.imshow('Posture corrector', frame)

cap.release()
cv2.destroyAllWindows()