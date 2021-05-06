from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class LoginForm(FlaskForm):
    email = StringField("Email", id="login__email")
    password = PasswordField("Password", id="login__password")
    remember_me = BooleanField("RememberMe", id="login__remember")
    submit = SubmitField("Submit", id="login__submit")


class RegistrationForm(FlaskForm):
    username = StringField("Username", id="registration__username")
    email = StringField("Email", id="registration__email")
    password = PasswordField("Password", id="registration__password")
    confirm_password = PasswordField("Check Password", id="registration__check-password")

    name 
    surname
    burthday
    gender
    current_location
    skill_level

