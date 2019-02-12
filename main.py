import numpy as np
import cv2

#cap = cv2.VideoCapture(0)
filename = 'video.avi'
frames_per_seconds = 30;
my_res = '4k'


def change_res(cap,width, height):
    cap.set(3, width)
    cap.set(4,height)

STD_DIMENSIONS = {
        "480p": (680, 480),
        "720p": (1280, 720),
        "1080p":(1920, 1080),
        "4k" :  (4120, 2160),
}

def get_dims(cap, res='1080p'):
    width,height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

cap = cv2.VideoCapture(0)
dims = get_dims(cap, res=my_res)

while True:
     
    ret, frame = cap.read()
    cv2.imshow('Frame1', frame)    #Displays the feed

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

#Release the feed 
cap.release()
cv2.destroyAllWindows()
