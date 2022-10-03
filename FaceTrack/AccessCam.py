import numpy as np
import cv2 as cv
import cv2
import imutils
import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils



cap = cv.VideoCapture(0)
#http://192.168.128.93:8080/video?type=some.mpeg


def textWrite(text, coord, bool):
        cv.putText(frame, 
                text, 
                (coord[0], coord[1]), 
                cv.FONT_HERSHEY_SIMPLEX, 0.8, 
                (0, 255, 255), 
                2, 
                cv.LINE_4, False)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=320)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    #COLOR_BGR2GRAY
    #COLOR_BGR2RGB
    #COLOR_RGB2BGR
    # Display the resulting frame
    textWrite("Amecar", (0, 20), True)   
    textWrite("fps: ", (0, 42), True)
    textWrite("60", (50, 42), True)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()