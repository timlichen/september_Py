from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
mysql = MySQLConnector(app, 'login_registration')
app.secret_key = 'key'
bcrypt = Bcrypt(app)


@app.route("/")
def index():
	return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
	flag = False
	email = request.form['email']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	password = request.form['password']
	confirm_password = request.form['confirm_password']

	if len(request.form['email']) < 1:
		flag = True
		flash("Name cannot be empty")
	elif not EMAIL_REGEX.match(request.form['email']):
		flag = True
		flash("Invalid Email Address")
	if len(request.form['first_name']) < 2:
		flag = True
		flash("first_name cannot be empty and must have at least 2 characters")
	elif request.form['first_name'].isalpha() == False:
		flag = True
		flash("Characters must be alphabetic")
	if len(request.form['last_name']) < 2:
		flag = True
		flash("last_name cannot be empty and must have at least 2 characters")
	elif request.form['last_name'].isalpha() == False:
		flag = True
		flash("Characters must be alphabetic")
	if len(request.form['password']) < 1:
		flag = True
		flash("password cannot be empty")
	elif (request.form['password'] != request.form['confirm_password']):
		flag = True
		flash("password and confirm_password do not match")
	elif not PASSWORD_REGEX.match(request.form['password']):
		flag = True
		flash("Password must be at least 8 characters and contain 1 number and 1 uppercase letter")
	if len(request.form['confirm_password']) < 1:
		flag = True
		flash("confirm_password cannot be empty")
	if not flag:
		flash('Successful Registration / login!')
		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		insert_query = "INSERT INTO login (email, first_name, last_name, password, created_at, updated_at) VALUES (:email, :first_name, :last_name, :pw_hash, NOW(), NOW())"
		query_data1 = {'email': request.form['email'], 'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'pw_hash': pw_hash }
		mysql.query_db(insert_query, query_data1)
		select_query = "SELECT * FROM login WHERE email= :email LIMIT 1"
		query_data2 ={'email': request.form['email']}
		user = mysql.query_db(select_query, query_data2)
		print user
		session['userkey'] = user[0]['id']
		return render_template('success_register.html', userkey=session['userkey'])
	else: 
		return redirect('/')
app.run(debug=True)