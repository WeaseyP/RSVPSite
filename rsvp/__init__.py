from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session


application = Flask(__name__)
application.static_folder = 'static'

application.config['SECRET_KEY'] = 'f88c7806fb1bbf7b00cecd48686074e5'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)

from rsvp import routes