import os

class Configuration:
    MAIL_SERVER = 'smtp.google.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'lucasmallmann76@gmail.com'
    MAIL_PASSWORD = '123'
    SECRET_KEY = os.environ.get('SECRET_KEY') or '88d37ca6166bf2bfbe59218d1d0e62bf'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
