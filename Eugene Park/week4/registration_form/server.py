from flask import Flask, render_template, request, flash, redirect
import re
app = Flask(__name__)
app.secret_key = 'the_time_is_a_flat_circle'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
CAP_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]*[A-Z]+[a-zA-Z0-9.+_-]*$')
NUM_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]*[0-9]+[a-zA-Z0-9.+_-]*$')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
		flash("No field can be empty!")
	if not NAME_REGEX.match(request.form['first_name']) or not NAME_REGEX.match(request.form['last_name']):
		flash("Name can only have letters!")
	if len(request.form['password']) < 8:
		flash("Password should be more than 8 characters")
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Not a valid email address")
	if not request.form['password'] == request.form['confirm_password']:
		flash("Passwords do not match")
	if not CAP_REGEX.match(request.form['password']):
		flash("Password should contain at least 1 uppercase")
	if not NUM_REGEX.match(request.form['password']):
		flash("Password should contain at least 1 numeric value")
	return redirect('/')

app.run(debug=True)