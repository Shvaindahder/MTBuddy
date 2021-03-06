from flask import redirect, url_for, request, render_template, flash
from flask_login import login_user, logout_user, current_user, login_required

from app import db
from app.utils import load_media
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from models.user import User


# @bp.route("/index", methods=["GET", "POST"])
# def auth_page():
#     if current_user.is_authenticated:
#         return redirect(url_for("main.index"))
#     login_form = LoginForm()
#     registration_form = RegistrationForm()

#     if login_form.validate_on_submit():
#         print("LOGIN FORM VALIDATES ON SUBMIT")
#         user = User.query.filter_by(email=login_form.email.data).first()
#         if user is None:
#             return redirect(url_for("auth.auth_page"))
#         login_user(user)
#         next_page = request.args.get("next")

#         if not next_page:
#             next_page = url_for("main.index")
#         return redirect(next_page)
    
#     if registration_form.validate_on_submit():
#         print("REGISTRATION FORM VALIDATES ON SUBMIT")
#         user = User(registration_form)
#         user.set_password(registration.password.data)
#         db.session.add(user)
#         db.session.commit()
#         print("New data")
#         return redirect(url_for("auth.auth_page"))

#     context = {
#         "title": "Auth Page",
#         "registration_form": registration_form,
#         "login_form": login_form
#     }
    
#     return render_template("auth/auth_page.html", **context)


@bp.route("/index")
def auth_page():
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))
    login_form = LoginForm()
    registration_form = RegistrationForm()
    context = {
        "title": "Auth Page",
        "registration_form": registration_form,
        "login_form": login_form
    }

    return render_template("auth/auth_page.html", **context)



@bp.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()
    

    user = User(form)
    user.set_password(form.password.data)
    
    if form.avatar.data is not None:
        filename = load_media(form.avatar.data)
        user.avatar = filename

    db.session.add(user)
    db.session.commit()
    
    flash("Registration success.")

    return redirect(url_for("auth.auth_page"))



@bp.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    if user is None:
        flash("Invaild email. Try again")
        return redirect(url_for("auth.auth_page"))
    if user.check_password(form.password.data):
        login_user(user)
        next_page = request.args.get("next")

        if not next_page:
            next_page = url_for("main.profile")
        return redirect(next_page)
    flash("Password isn't correct")
    return redirect(url_for("auth.auth_page"))


@login_required
@bp.route("/logout")
def logout():
    logout_user()
    flash("User logout")
    return redirect(url_for("auth.auth_page"))


