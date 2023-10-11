from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


secret_key = os.urandom(12)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fly2.db"
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)
from fly_app.routes import airports_bp, passengers_bp, flights_bp

app.register_blueprint(airports_bp)
app.register_blueprint(passengers_bp)
app.register_blueprint(flights_bp)
# login = LoginManager(app)


from fly_app import routes
from fly_app import models

with app.app_context():
    db.create_all()
