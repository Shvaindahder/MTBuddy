from typing import Optional
from flask_login.mixins import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.auth.forms import RegistrationForm


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, nullable=False)
    surname = db.Column(db.String(32), index=True, nullable=False)

    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    gender = db.Column(db.Boolean)
    birthday = db.Column(db.DateTime, nullable=True)
    current_location = db.Column()

    avatar = db.Column(db.String(128), nullable=True)

    def __init__(self, form=Optional[RegistrationForm] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if form != None:
            self.__fill_from_form(form)

    def __fill_from_form(self, registration_form: RegistrationForm):
        self.name = registration_form.name.data
        self.surname = registration_form.name.data

        self.username = registration_form.username.data
        self.email = registration_form.email.data
        
        self.gender = registration_form.gender.data
        self.birthday = registration_form.birthday.data
        self.current_location = registration_form.current_location.data

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
    