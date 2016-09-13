from flask import Flask, render_template, request, redirect, flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from mysqlconnection import MySQLConnector

app = Flask(__name__)

app.secret_key = 'key'

mysql = MySQLConnector(app, 'emails')

@app.route("/")
def index():
	return render_template("index.html", )

@app.route("/email", methods=['POST'])
def getEmail():
	flag = False
	if len(request.form["email"]) < 1:
		flag = True
		flash("name cannot be empty")
	if not EMAIL_REGEX.match(request.form['email']):
		flag = True
		flash("email address entered incorrectly")
	if flag == True:
		return redirect('/')
	else:
		email = request.form['email']
		print email
		query = ("INSERT INTO emails (emails, updated_at, created_at) VALUES (:email, NOW(), NOW());")
		data = { 'email': email}
		if mysql.query_db(query, data):
			print "Successful!"
		return redirect('/success')
@app.route("/success")
def success():
	query = "SELECT * from emails"
	emails = mysql.query_db(query)
	return render_template("success.html", emails=emails)
app.run(debug=True)