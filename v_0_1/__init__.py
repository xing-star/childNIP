from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config, DevelopmentConfig, ProductionConfig
from flask_cors import CORS

db = SQLAlchemy()

config_name = config['default']

app = Flask(__name__)
app.config.from_object(config_name)
config_name.init_app(app)
db.init_app(app)

CORS(app)

from .misapp.urls import approuter
approuter()
