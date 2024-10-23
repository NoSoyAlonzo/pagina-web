from flask import Flask
from config import Config
from singleton_db import SingletonDB

app = Flask(__name__)
app.config.from_object(Config)

db = SingletonDB()
db.init_app(app)

from app import routes
