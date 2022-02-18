from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import config_options

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options['development'])
    
    db.init_app(app)
    ma.init_app(app)

    from app.main.v1 import main
    app.register_blueprint(main)

    return app

