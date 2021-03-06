from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, EqualTo 


class LoginForm(FlaskForm):
    email = StringField("Email", id="login__email", validators=[DataRequired()])
    password = PasswordField("Password", id="login__password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me", id="login__remember")
    forgot = SubmitField("Forgot", id="login__forgot")
    submit = SubmitField("Submit", id="login__submit")


class RegistrationForm(FlaskForm):
    avatar = FileField("Profile Pic", id="registration__file", validators=[FileAllowed(["jpg", "png"], "Images only.")])

    username = StringField("Username", id="registration__username", validators=[DataRequired()])
    email = StringField("Email", id="registration__email", validators=[DataRequired()])
    password = PasswordField("Password", id="registration__password", validators=[DataRequired()])
    confirm_password = PasswordField("Check Password", id="registration__check-password", validators=[DataRequired(), EqualTo("password")])

    name = StringField("Name", id="registration__name", validators=[DataRequired()])
    surname = StringField("Surname", id="registration__surname", validators=[DataRequired()])
    birthday = DateField("Burthday", id="registration__burthday", validators=[DataRequired()])
    gender = RadioField("Gender", choices=["Male", "Female"], id="registration__gender")
    current_location = StringField("Current Location", id="registration__current-location")
    skill_level = SelectField("Skill Level", choices=list(range(1, 6)), id="registration__skill-level")

    submit = SubmitField("Submit", id="registration__submit")

