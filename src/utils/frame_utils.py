import cv2
def draw_detections(frame, detections):
    for d in detections:
        x,y = d["pos"]
        cv2.circle(frame, (x,y), 6, (0,255,0), 1)