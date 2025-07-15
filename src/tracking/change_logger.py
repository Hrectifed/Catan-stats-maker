import json, pathlib, time
LOG_PATH = pathlib.Path("logs")
LOG_PATH.mkdir(exist_ok=True)
class ChangeLogger:
    def __init__(self, game_id="game1"):
        self.fp = open(LOG_PATH / f"{game_id}_log.jsonl", "w")
    def log(self, event):
        self.fp.write(json.dumps(event) + "\n")
        self.fp.flush()