import numpy as np
import cv2 as cv
import cv2
import time
from datetime import datetime
import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates


## A little different from my initial faceTracker, this one removes the 
## drawn boxes and captures an image when a face is detected.
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
currTime = 0
prevTime = 0

def captureOnDetect():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d%m%Y%H%M%S")
    print(dt_string)
    return dt_string

def textWrite(text, coord, bool):
        cv.putText(image, 
                text, 
                (coord[0], coord[1]), 
                cv.FONT_HERSHEY_SIMPLEX, 0.8, 
                (0, 255, 255), 
                2, 
                cv2.LINE_AA, bool)

cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
  while cap.isOpened():
    currTime = time.time()
    success, image = cap.read()
    success, image1 = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections:
        #mp_drawing.draw_detection(image, detection)
        textWrite("Face detected", (0, 20), False)
        cv2.imshow('MediaPipe Face Detection', image)
        if currTime - prevTime > 5 :
            #cv2.imwrite('img_'+ captureOnDetect()+'.jpg', image) Draws over pixels, the other doesn
            cv2.imwrite('img1_'+ captureOnDetect()+'.jpg', image1)
            prevTime = currTime
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()