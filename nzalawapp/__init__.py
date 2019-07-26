from flask import Flask

import os
from flask_login import LoginManager


app = Flask(__name__)
login_manager=LoginManager(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config["SQLALCHAMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = "you will never guess"