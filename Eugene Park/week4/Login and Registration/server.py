from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'carcosa'
mysql = MySQLConnector(app, 'login_reg')
bcrypt = Bcrypt(app)

@app.before_first_request
def run_server():
	session['name'] = ''
	session['email'] = ''

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
	flag = False
	if len(request.form['first_name']) < 2:
		flag = True
		flash("First name is too short")
	if not NAME_REGEX.match(request.form['first_name']):
		flag = True
		flash("First name can only be letters")
	if len(request.form['last_name']) < 2:
		flag = True
		flash("Last name is too short")
	if not NAME_REGEX.match(request.form['last_name']):
		flag = True
		flash("Last name can only be letters")
	if not EMAIL_REGEX.match(request.form['email']):
		flag = True
		flash('Invalid Email address')
	if request.form['password'] < 8:
		flag = True
		flash('password need to be at least 8 characters')
	if not request.form['password'] == request.form['password_con']:
		flag = True
		flash('password does not match')
	if flag:
		return redirect('/')
	else:
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email = request.form['email']
		password = bcrypt.generate_password_hash(request.form['password'])
		query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now())'
		data = {
				"first_name": first_name,
				"last_name": last_name,
				"email": email,
				"password": password
		}
		mysql.query_db(query, data)
		session['name'] = str(first_name) +" "+ str(last_name)
		session['email'] = email
		return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	query = "SELECT * FROM users WHERE email LIKE :email LIMIT 1"
	data = {'email': email}
	user = mysql.query_db(query, data)
	if bcrypt.check_password_hash(user[0]['password'], password):
		session['name'] = str(user[0]['first_name']) +" "+ str(user[0]['last_name'])
		session['email'] = user[0]['email']
		return redirect('/success')
	else:
		flash('Unable to login')
		return redirect('/')

@app.route('/success')
def success():
	return render_template('success.html')

app.run(debug=True)