"""HSV ranges and general configuration."""
HSV_RANGES = {
    # (H_low, S_low, V_low), (H_high, S_high, V_high)
    "red":    ((0, 120, 70),  (10, 255, 255)),
    "blue":   ((100, 150, 50), (130, 255, 255)),
    "white":  ((0, 0, 200),   (180, 30, 255)),
    "orange": ((10, 150, 100),(25, 255, 255)),
    "green":  ((45, 100, 40), (75, 255, 255)),
    "brown":  ((10, 50, 20),  (20, 200, 150)),
}
STABLE_FRAMES = 8  # minimum frames before confirming change
DICE_ROI = (0.70, 0.05, 0.28, 0.20)  # relative x,y,w,h