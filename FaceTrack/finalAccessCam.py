import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

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
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

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