from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]+$')
app = Flask(__name__)
app.secret_key='Secret' 
@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')
@app.route('/process', methods = ['POST'])
def process():
	success = True
	if len(request.form['email'])<1:
		flash('Email cannot be empty!')
		success = False
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email Address!')
		success = False
	if len(request.form['firstname'])<1:
		flash('First name cannot be empty!')
		success = False
	elif not NAME_REGEX.match(request.form['firstname']):
		flash('First name must only contain letters')
		success = False
	if len(request.form['lastname'])<1:
		flash('Last name cannot be empty!')
		success = False
	elif not NAME_REGEX.match(request.form['lastname']):
		flash('Last name must only contain letters')
		success = False
	if len(request.form['password']) <8:
		flash('Password must have 8 or more characters')
		success = False
	elif not PASSWORD_REGEX.match(request.form['password']):
		flash('Password must have at least 1 uppercase letter and 1 numeric value')
		success = False
	elif not request.form['password'] == request.form['passwordconfirm']:
		flash('Passwords must match')
		success = False
	if success == True:
		flash('Thanks for submitting your information.')
	return redirect('/')
app.run(debug=True)