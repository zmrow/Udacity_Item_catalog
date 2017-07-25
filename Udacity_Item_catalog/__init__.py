import os
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# _basedir = os.path.abspath(os.path.dirname(__file__))
#DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'flask-website.db'))'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'catalog.db')

db = SQLAlchemy(app)

import Udacity_Item_catalog.models
