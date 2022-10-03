import urllib.request
import cv2

url = 'http://192.168.128.93:8080/video?type=some.mpeg'
video, http = urllib.request.urlretrieve(url)
cap = cv2.VideoCapture(video)


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
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()