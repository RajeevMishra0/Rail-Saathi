# Application routes
from flask import render_template, redirect, url_for
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    # Train search logic (Rajeev Mishra)
    return render_template('search.html')
