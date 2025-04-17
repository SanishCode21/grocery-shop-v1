from dotenv import load_dotenv
import os
from flask import current_app as app

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')  # Use a fallback default
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///Grocery_db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

