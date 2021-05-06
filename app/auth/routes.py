from flask import redirect, url_for, request, render_template
from flask_login import login_user, logout_user, current_user

from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from models.user import User


@bp.route("/main", methods=["GET", "POST"])
def auth_page():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is None:
            return redirect(url_for("auth.auth_page"))
        login_user(user)
        next_page = request.args.get("next")

        if not next_page:
            next_page = url_for("main.index")
        
        return redirect(next_page)
    
    if registration_form.validate_on_submit():
        user = User(registration_form)
        user.set_password(registration.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.auth_page"))

    context = {
        "title": "Auth Page",
        "registration_form": registration_form,
        "login_form": login_form
    }
    
    return render_template("auth_page.html", context)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.auth_page"))


