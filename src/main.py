"""
Entry point: captures webcam/video, runs detectors, updates GameState
Usage:
python -m src.main --camera 0
python -m src.main --video data/sample.mp4
"""
import argparse, cv2, time
from src.tracking.game_state import GameState
from src.detector.color_detect import detect_pieces
from src.detector.occlusion import is_occluded
from src.utils.frame_utils import draw_detections

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--camera", type=int, default=None)
    p.add_argument("--video", type=str, default=None)
    p.add_argument("--demo", action="store_true")
    return p.parse_args()

def main():
    args = parse_args()
    if args.demo:
        # For demo mode, use camera 0 as default
        source = 0
    else:
        source = args.camera if args.camera is not None else args.video
    cap = cv2.VideoCapture(source)
    gs = GameState()
    reference = None
    while True:
        ok, frame = cap.read()
        if not ok: break
        frame = cv2.flip(frame, 1)  # mirror for convenience
        if reference is None:
            reference = frame.copy()
        if not is_occluded(frame, reference):
            detections = detect_pieces(frame)
            events = gs.update(detections)
            # TODO: write events to logger
            # Draw detections overlay on the frame
            draw_detections(frame, detections)
        cv2.imshow("Catan Vision", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()