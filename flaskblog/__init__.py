import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '88d37ca6166bf2bfbe59218d1d0e62bf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# Passando a view responsável por realizar o login
login_manager.login_view = 'login'
login_manager.login_message = 'Please, you have to login to view this page'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.google.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lucasmallmann76@gmail.com'
app.config['MAIL_PASSWORD'] = '123'
flask_mail = Mail(app)

from flaskblog import routes
