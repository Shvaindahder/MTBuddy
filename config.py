import os
from dotenv import load_dotenv


BASEDIR = os.path.abspath('.')
UPLOAD_FOLDER = os.path.join(BASEDIR, "media")
load_dotenv(os.path.join(BASEDIR, ".env"))


class Config:
    DEBUG = os.environ.get("DEBUG") or True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "9805d06e7a953055f70448c07f89a7b27a32ab224c3d9c284bd403a1ccb7a7b0"
    TEMPLATES_FOLDER = os.path.join(BASEDIR, "templates") 
    STATICFILES_FOLDER = os.path.join(BASEDIR, "static")
    UPLOAD_FOLDER = UPLOAD_FOLDER
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or f"sqlite:///{os.path.join(BASEDIR, 'data.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
