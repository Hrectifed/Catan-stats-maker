import cv2
import numpy as np

def draw_detections(frame, detections):
    """Draw detection overlays on the frame with color-coded labels."""
    # Color mapping for different piece colors
    color_map = {
        "red": (0, 0, 255),
        "blue": (255, 0, 0), 
        "white": (255, 255, 255),
        "orange": (0, 165, 255),
        "green": (0, 255, 0),
        "brown": (42, 42, 165)
    }
    
    for d in detections:
        x, y = d["pos"]
        color = d["color"]
        piece_type = d["type"]
        
        # Use the piece color for the overlay, defaulting to green
        draw_color = color_map.get(color, (0, 255, 0))
        
        # Draw different shapes based on piece type
        if piece_type == "road":
            # Draw a rectangle for roads
            cv2.rectangle(frame, (x-15, y-5), (x+15, y+5), draw_color, 2)
        elif piece_type == "city":
            # Draw a larger circle for cities
            cv2.circle(frame, (x, y), 12, draw_color, 2)
        else:  # settlement
            # Draw a medium circle for settlements
            cv2.circle(frame, (x, y), 8, draw_color, 2)
        
        # Add text label
        label = f"{color} {piece_type}"
        # Get text size for background
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        
        # Draw text background
        cv2.rectangle(frame, (x-text_width//2-2, y-25-text_height-2), 
                     (x+text_width//2+2, y-25+baseline), (0, 0, 0), -1)
        
        # Draw text
        cv2.putText(frame, label, (x-text_width//2, y-25), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, draw_color, 1, cv2.LINE_AA)