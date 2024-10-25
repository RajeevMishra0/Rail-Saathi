import os
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
import pymysql
pymysql.install_as_MySQLdb()

basedir = os.path.abspath(os.path.dirname(__file__))  # Get the absolute path to the current directory
app = Flask(__name__,template_folder=os.path.join(basedir, 'templates'), static_folder=os.path.join(basedir, 'static'))


# If you have any database-related configurations or setups
DATABASE_FOLDER = 'database'
database_config_path = os.path.join(basedir, '../database/config.py')
app.config.from_pyfile(database_config_path)

# Initialize database and CSRF protection
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db)
# Application routes
@app.route('/')
def home():
    print("Home route accessed")  # Add this line
    print("Template folder:", app.template_folder)
    print("Available templates:", os.listdir(app.template_folder))
    return render_template('index.html')

@app.route('/register')
def register():
    # Your registration logic here
    return render_template('register.html')


@app.route('/search')
def search():
    # Train search logic (Rajeev Mishra)
    return render_template('search.html')

@app.route('/login', endpoint='login')  # Rename the endpoint to avoid conflicts
def login_route():
    # Login functionality here
    return render_template('login.html')

@app.route('/forgot_password')
def forgot_password():
    # Login functionality here
    return render_template('forgot_password.html')

@app.route('/logout')
def logout():
    # Logic for logging out a user
    return redirect(url_for('home'))

@app.route('/contact_us')
def contact_us():
    return render_template('contact-us.html')

@app.route('/booking')
def booking():
    # Your booking logic here
    return render_template('booking.html')

@app.route('/history')
def history():
    # Your history logic here
    return render_template('history.html')

@app.route('/dashboard')
def dashboard():
    # Your dashboard logic here
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
