from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    surname = db.Column()

    username = 
    email = 
    password = 

    gender = db.Column()
    birthday = db.Column()
    current_location = db.Column()
    