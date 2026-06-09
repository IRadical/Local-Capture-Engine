import json
from pathlib import Path
from flask import Flask, render_template

ruta_config = Path(__file__).parent / "config" / "config.json"
with open(ruta_config, "r") as f:
    config = json.load(f)

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",
                           nombre_proyecto=config["configuracion"]["nombre_proyecto"],)

if __name__ == "__main__":
    puerto = config["configuracion"]["pto_flask"]
    app.run(host="0.0.0.0", port=puerto, debug=True)
