from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


secret_key = os.urandom(12)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fly2.db"
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)


from fly_app import routes
from fly_app import models

with app.app_context():
    db.create_all()
