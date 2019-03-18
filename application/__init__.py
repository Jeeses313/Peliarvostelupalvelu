from flask import Flask
app = Flask(__name__)

from application import views

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from application.games import views
from application.games import models


db.create_all()
