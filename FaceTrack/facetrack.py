from cmath import rect
from ftplib import FTP_TLS
import cv2
import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates

#This code successfully detects a face and outputs a message 


# Actual software to drive Amecar
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

fps = 0

def centerThirdBox(width, height):
  #This box will be the center third indicator
  #to compare the image to.
  width3 = width*(1/3)
  height3 = height*(1/3)
  width4 = width*(2/3)
  height4 = height*(2/3)


  print(f'third is{width3, height3, width4, height4}')



def distFromCenter(width, height, fps, boxDist):
#tells distances from center
    centerWidth= width*(0.5/1.0)
    centerHeight = height*(0.5/1.0)
    print(f'center{centerWidth, centerHeight}')
    newXmin = (0.5 - (boxDist.width/2))
    newYmin = (0.5 - (boxDist.height/2))
    newXmax = (0.5 + (boxDist.width/2))
    newYmax = (0.5 + (boxDist.height/2))
    #There is need to make sure that the widths don't vary much for the
    #zooms that may occur. The boxes vary with zooming.
    print(f'new Xmin, Ymin, Xmax, Ymax{newXmin, newYmin, newXmax, newYmax }')
    x=  _normalized_to_pixel_coordinates(newXmin, newYmin, width,height)
    y=  _normalized_to_pixel_coordinates(newXmax, newYmax, width, height)
    print(f'normalize{x, y}')
    # x = (266, 186) y = (373, 293)
    cv2.rectangle(image,x , y, (255,35,0), 2)
    print(f'FACE in Dst: \n{boxDist.xmin , boxDist.ymin, boxDist.width, boxDist.height}')
    print(f'Face{width, height, fps, boxDist}')

def textWrite(text, coord, bool):
        cv2.putText(image, 
                text, 
                (coord[0], coord[1]), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
                (0, 255, 255), 
                2, 
                cv2.LINE_AA, bool)   

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.1) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    image_copy = image.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    #textWrite(text   , (x, y), False)
    textWrite("Amecar", (10, 30), False)
    textWrite(str(fps), (10, 65), False)
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)
    
    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    FACIAL_KEYPOINTS = mp.solutions.face_detection.FaceKeyPoint
    # print(FACIAL_KEYPOINTS)
    if results.detections:
      #  face_data = face.location_data
      #  print(f'nFace Bounding Box: n {face_data.relative_bounding_box}')
       textWrite("Face detected", (240, 425), False)
       for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
        print(width, height, fps)
        cv2.rectangle(image, (280, 200), (360, 280), (0,0,255), 1)
        for face_no, face in enumerate(results.detections):
          face_data = face.location_data
          print(face_data.relative_bounding_box)
          distFromCenter(width, height,fps, face_data.relative_bounding_box)
          centerThirdBox(width, height)
          # print(f'FACE BOUNDING BOX: \n{face_data.relative_bounding_box}')
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Detection', image)
    #cv2.rotate(img, cv2.ROTATE_180)
    #cv2.flip(image, 0)
    
    
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()