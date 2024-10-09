# Flask app initialization
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config.from_pyfile('../database/config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# You can keep any other imports here if needed, but routes are now in app.py