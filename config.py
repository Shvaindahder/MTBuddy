import os


BASEDIR = os.path.abspath('.')


class Config:
    DEBUG = os.environ.get("DEBUG") or True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "9805d06e7a953055f70448c07f89a7b27a32ab224c3d9c284bd403a1ccb7a7b0"
    TEMPLATES_FOLDER = os.path.join(BASEDIR, "templates") 
    STATICFILES_FOLDER = os.path.join(BASEDIR, "static")
    MEDIAFILES_FOLDER = os.path.join(BASEDIR, "media")
    DATABASE = os.path.join("DATABASE_URI") or f"sqlite:///{os.path.join(BASEDIR, "app.db")}"
