from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI','postgres_url_here')
    SECRET_KEY = 'Clave'
    SQLALCHEMY_TRACK_MODIFICATIONS = False