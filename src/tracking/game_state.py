class GameState:
    """Graph of intersections/edges & what piece occupies each."""
    def __init__(self):
        self.state = {}          # key = board_coord, value = (color, type)
    def update(self, detections):
        """Compute diff with previous frame, return list of events."""
        events = []
        # TODO: implement diff logic + stability buffer
        return events