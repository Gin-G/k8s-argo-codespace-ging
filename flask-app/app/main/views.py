from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/templates/navbar.html')
def navbar():
    return render_template('navbar.html')