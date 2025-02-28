#VisionFlow

#Created by VortexCyber 
#LinkTree: http://linktr.ee/vortex_ 

#Link installation app IP Camera:
#Android: https://play.google.com/store/apps/details?id=com.pas.webcam
#iPhone: https://apps.apple.com/us/app/epoccam-webcam/id1534160801

import cv2

# YOUR IP CAMERA (example: http://999.999.999.999/video)
url = "" 

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: unable to connect to the video stream.")
    exit()

print("Video stream connected successfully!")

def adjust_brightness(frame, brightness=1.0):
    frame = cv2.convertScaleAbs(frame, alpha=brightness, beta=0)
    return frame

cv2.namedWindow("Video stream", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Video stream", 800, 600)

cv2.createTrackbar("Luminosity", "Video stream", 10, 30, lambda x: None)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: unable to read frame.")
        break
    brightness = cv2.getTrackbarPos("Luminosity", "Video stream") / 10.0
    frame = adjust_brightness(frame, brightness)
    cv2.imshow("Video stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
