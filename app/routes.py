from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
	return render_template('welcome.html',title='Home')

@app.route('/index')
def index():
	return "<h1>Index</h1>"
