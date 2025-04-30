import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = FLASK_ENV == 'development'
    PORT = int(os.getenv('PORT', 5000))