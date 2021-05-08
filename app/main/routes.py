from flask import redirect, render_template, url_for, request
from flask_login import login_required, current_user

from app import db
from app.auth.forms import RegistrationForm, LoginForm
from app.main import bp
from app.main.forms import ProfileSettingsForm
from app.utils import load_media


@bp.route("/about-us")
def about_us():
    if current_user.is_authenticated:
        context = {
            "title": "About US"
        }
    else:
        context = {
            "title": "About us",
            "registration_form": RegistrationForm(),
            "login_form": LoginForm()
        }
    return render_template("main/about.html", **context)


@login_required
@bp.route("/profile-page")
def profile():
    context = {
        "name": current_user.get_name(),
        "title": "Profile"
    }
    return render_template("main/profile_page.html", **context)


@login_required
@bp.route("/profile-settings", methods=["GET", "POST"])
def profile_settings():
    form = ProfileSettingsForm()
    if form.validate_on_submit():
        if form.username.data:
            current_user.username = form.username.data
        if form.email.data:
            current_user.email = form.email.data
        if form.password.data:
            current_user.set_password(form.password.data)
        current_user.skill_level = form.skill_level.data
        if form.avatar.data and form.avatar.data != current_user.avatar:
            print(form.avatar.data.filename)
            filename = load_media(form.avatar.data)
            current_user.avatar = filename
        db.session.commit()
        return redirect(url_for("main.profile_settings"))
    context = {
        "title": "Profile Settings",
        "form" : form
    }
    return render_template("main/profile_settings.html", **context)