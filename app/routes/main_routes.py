from flask import Blueprint

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return "pantalla principal"

@main_bp.route("/<seccion>")
def vista_seccion(seccion):
    return f"vista_seccion: {seccion}"

@main_bp.route("/<seccion>/<item>")
def vista_item(seccion, item):
    return f"vista_item: {item}"