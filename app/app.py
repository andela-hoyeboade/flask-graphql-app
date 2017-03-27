import os

from flask import Flask

app = Flask(__name__)

BASEDIR = os.path.abspath(os.path.dirname(__file__))

if os.getenv('HEROKU'):
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')
