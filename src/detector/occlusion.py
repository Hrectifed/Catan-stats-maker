import cv2, numpy as np
def is_occluded(frame, reference, threshold_px=40_000):
    diff = cv2.absdiff(frame, reference)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    return np.count_nonzero(gray > 50) > threshold_px