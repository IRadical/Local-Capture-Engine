from app.utils.config_loader import config
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html", secciones=config["secciones"], nombre_proyecto=config["configuracion"]["nombre_proyecto"], colores=config["colores"])

@main_bp.route("/<seccion>")
def vista_seccion(seccion):
    return f"vista_seccion: {seccion}"

@main_bp.route("/<seccion>/<item>")
def vista_item(seccion, item):
    return f"vista_item: {item}"