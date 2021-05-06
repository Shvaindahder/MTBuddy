from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="auth")

from app.auth import routes