import os
import sqlite3
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
    g
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'catalog.db')

db = SQLAlchemy(app)

from models import User, Category, Item

@app.route('/')
def index():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
