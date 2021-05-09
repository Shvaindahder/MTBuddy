from config import UPLOAD_FOLDER
from flask import Blueprint
from flask import redirect, url_for
from flask_login import current_user

bp = Blueprint("index", __name__)

@bp.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))
    return redirect(url_for("auth.auth_page"))