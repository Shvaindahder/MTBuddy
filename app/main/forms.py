from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email


class ProfileSettingsForm(FlaskForm):
    avatar = FileField("Profile image", id="profile-settings__avatar", validators=[FileAllowed(["jpg", "png"], "Images only")])
    skill_level = SelectField("Skill Level: ", choices=list(range(0, 6)))

    username = StringField("Change username: ", id="profile-settings__username")
    email = StringField("Change email: ", id="profile-settings__email")
    password = PasswordField("New password: ", id="profile-settings__password")
    confirm_password = PasswordField("Confirm Password: ", id="profile-settings__check-password", validators=[EqualTo("password")])

    submit = SubmitField("Save: ", id="profile-settings__submit")
