from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'Secret'
mysql = MySQLConnector(app, 'email_validation')
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/email', methods = ['POST'])
def add():
	if len(request.form['email']) < 1:
		flash("Email is not valid!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Email is not valid!")
	else:
		flash('The email address you entered ('+request.form['email']+") is a VALID email address! Thank you!")
		query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
		data = {
			'email': request.form['email']
		}
		mysql.query_db(query,data)
		return redirect('/success')
	return redirect('/')
@app.route('/success')
def list():
	emails = mysql.query_db("SELECT * FROM users ORDER BY created_at DESC")
	print emails
	return render_template('success.html', all_emails = emails)
@app.route('/remove/<email_id>', methods = ['POST'])
def delete(email_id):
	query = "DELETE FROM users WHERE id = :id"
	data = {'id': email_id}
	mysql.query_db(query,data)
	return redirect('/success')
app.run(debug = True)