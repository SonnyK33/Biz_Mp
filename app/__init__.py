from flask import Flask, config



def create_app(config_class=config):
    app = Flask(__name__)

    app.config.from_object(config_class)
    
    #register blueprints:
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
