from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'golden'
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/validateEmail', methods=['POST'])
def validator():
	flag = False
	if len(request.form['email']) == 0:
		flag = True
		flash("Email field cannot be blank")
	if not EMAIL_REGEX.match(request.form['email']):
		flag = True
		flash('Email is not valid.')
	if flag:
		return redirect('/')
	else:
		email = request.form['email']
		print email
		query = 'INSERT into emails (email, created_at, updated_at) values (:email, now(), now())'
		session['email'] = email
		data = {"email": email}
		if mysql.query_db(query, data):
			print 'sucessfully saved to database'
		return redirect('/success')

@app.route('/success')
def success():
	query = "SELECT * from emails"
	emails = mysql.query_db(query)
	return render_template('success.html', emails = emails)

app.run(debug=True)