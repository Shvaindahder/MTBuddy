from flask import redirect, url_for
from flask_login import login_user, logout_user, current_user

from app.auth import bp

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    pass


@bp.route("/registration", methods=["GET", "POST"])
def registration():
    
