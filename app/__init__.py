from flask import Flask, current_app
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    


    
    #register blueprints:
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # check if this fixes path issue for auth package:
    # from app.auth import bp as auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')


    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)



    return app

from app import models 
