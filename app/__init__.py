import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.auth_page"
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__, template_folder=config_class.TEMPLATES_FOLDER, static_folder=config_class.STATICFILES_FOLDER)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    cors.init_app(app)

    from app.auth import bp as auth_bp
    from app.main import bp as main_bp
    from app.meeting import bp as meet_bp
    from app.index_routes import bp as index_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(meet_bp)
    app.register_blueprint(index_bp)

    return app



