import json
from pathlib import Path
from flask import Flask, render_template
from app.routes.main_routes import main_bp

ruta_config = Path(__file__).parent / "config" / "config.json"
with open(ruta_config, "r") as f:
    config = json.load(f)

app = Flask(__name__)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    puerto = config["configuracion"]["pto_flask"]
    app.run(host="0.0.0.0", port=puerto, debug=True)
