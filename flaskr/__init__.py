from flask import Flask

from config import Config
from flaskr.routes.loan_routes import loan_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(loan_bp, url_prefix='/api/loan')
    return app