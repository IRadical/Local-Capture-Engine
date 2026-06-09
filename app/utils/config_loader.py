import json
from pathlib import Path

ruta_config = Path(__file__).parent.parent.parent / "config" / "config.json"
with open(ruta_config, "r") as f:
    config = json.load(f)
