from flask import redirect, render_template
from flask_login import login_required, current_user

from app.main import bp
from app.main.forms import ProfileSettingsForm
from app.utils import load_media


@bp.route("/about-us")
def about_us():
    return render_template("main/about_us.html", title="About Us")


@login_required
@bp.route("/profile-page")
def profile():
    context = {
        "name": current_user.get_name(),
        "title": "Profile"
    }
    return render_template("main/profile_page.html", **context)


@login_required
@bp.route("/login-settings")
def profile_settings():
    form = ProfileSettingsForm()
    if form.validate_on_submit():
        print(form)
        return redirect("main.profile_settings")