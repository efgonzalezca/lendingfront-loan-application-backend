from flask import Flask
from flask_cors import CORS

from config import Config
from flaskr.routes.loan_routes import loan_bp
from flaskr.middlewares.error_handler import register_error_handlers

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    register_error_handlers(app)
    app.register_blueprint(loan_bp, url_prefix='/api/loan')
    return app