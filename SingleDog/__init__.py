# -*- encoding=UTF-8 -*-
import sys
sys.path.append('C:/MyCode/Python/MyProjects/NowCoder/junior/Single_0.0.1/SingleDog')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
app.secret_key = 'nowcoder'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = '/regloginpage/'

from SingleDog import views, models
