import os           #To find out what files we are using 
import numpy as np
import cv2

filename = 'video.mp4'
frames_per_seconds = 30;
my_res = '720p'


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


VIDEO_TYPE = {
        'avi' : cv2.VideoWriter_fourcc(*'MPEG'),
        'mp4' : cv2.VideoWriter_fourcc(*'MPEG'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']



cap = cv2.VideoCapture(0)
dims = get_dims(cap, res=my_res)
video_type_cv2 = get_video_type(filename)

out = cv2.VideoWriter(filename, video_type_cv2, frames_per_seconds, dims) #width, height

while True:
     
    #Provides frames 
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('Frame1', frame)    #Displays the feed

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

#Release the feed 
cap.release()
out.release()
cv2.destroyAllWindows()
