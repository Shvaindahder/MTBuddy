import os
from dotenv import load_dotenv


BASEDIR = os.path.abspath('.')
load_dotenv(os.path.join(BASEDIR, ".env"))


class Config:
    DEBUG = os.environ.get("DEBUG") or True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "9805d06e7a953055f70448c07f89a7b27a32ab224c3d9c284bd403a1ccb7a7b0"
    TEMPLATES_FOLDER = os.environ.get(BASEDIR, "templates") 
    STATICFILES_FOLDER = os.environ.get(BASEDIR, "static")
    MEDIAFILES_FOLDER = os.environ.get(BASEDIR, "media")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or f"sqlite:///{os.path.join(BASEDIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
