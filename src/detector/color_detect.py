import cv2, numpy as np
from src.config import HSV_RANGES

def get_color_mask(hsv, color):
    lo, hi = HSV_RANGES[color]
    return cv2.inRange(hsv, np.array(lo), np.array(hi))

def detect_pieces(frame):
    """Return list of dicts: [{'pos': (x,y), 'color': 'red', 'type': 'settlement'}]"""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    detections = []
    for color in HSV_RANGES:
        mask = get_color_mask(hsv, color)
        contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            area = cv2.contourArea(c)
            x,y,w,h = cv2.boundingRect(c)
            ratio = max(w,h)/max(1,min(w,h))
            if area < 150:  # ignore noise
                continue
            if ratio > 3:
                piece_type = "road"
            elif area > 1200:
                piece_type = "city"
            else:
                piece_type = "settlement"
            detections.append({"pos": (x+w//2, y+h//2), "color": color, "type": piece_type})
    return detections