from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, SelectField


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

    name = StringField("Name", id="registration__name")
    surname = StringField("Surname", id="registration__surname")
    burthday = DateField("Burthday", id="registration__burthday")
    gender = RadioField("Gender", choices=["Male", "Female"], id="registration__gender")
    current_location = StringField("Current Location", id="registration__current-location")
    skill_level = SelectField("Skill Level", choices=list(range(1, 6)), id="registration__skill-level")

