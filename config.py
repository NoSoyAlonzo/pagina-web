import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Alonso181437@localhost:3306/generador_nombres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
