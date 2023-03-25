from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fly.db"
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from fly_app import routes
from fly_app import models