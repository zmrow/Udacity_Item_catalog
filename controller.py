import os
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('Udacity_Item_catalog.config.DevelopmentConfig')
app.config.from_object('config.DevelopmentConfig')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'catalog.db')

db = SQLAlchemy(app)

import models
import views

if __name__ == '__main__':
    app.run()
