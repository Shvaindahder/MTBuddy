from flask import Blueprint

bp = Blueprint("meeting", __name__, url_prefix="/meeting")

from app.meeting import routes