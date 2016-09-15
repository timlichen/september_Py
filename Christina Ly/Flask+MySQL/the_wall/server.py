from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
app = Flask(__name__)
app.secret_key = 'Secret'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'the_wall')
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/user', methods=['POST'])
def register():
	if len(request.form['first_name']) <2:
		flash("Must enter valid first name!")
	elif not NAME_REGEX.match(request.form['first_name']):
		flash("First name must only contain letters")
	elif len(request.form['last_name']) <2:
		flash("Must enter valid last name!")
	elif not NAME_REGEX.match(request.form['last_name']):
		flash("Last name must only contain letters")
	elif len(request.form['email']) < 1:
		flash("Email is not valid!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Email is not valid!")
	elif len(request.form['password']) <8:
		flash("Password must be at least 8 characters")
	elif request.form['password'] != (request.form['confirm']):
		flash("Passwords must match")
 	else:
 		flash("You have successfully registered!")
 		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
		data = {'first_name':request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'pw_hash': pw_hash }
		mysql.query_db(query, data)
 		user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
		query_data = { 'email': request.form['email']}
		user = mysql.query_db(user_query, query_data)
		session['loggedin'] = user[0]['id']
		return redirect ('/wall')
	return redirect('/')
@app.route('/loginvalidate', methods=['POST'])
def validate():
	email = request.form['email']
	password = request.form['password']
	user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	query_data = { 'email': email }
	user = mysql.query_db(user_query, query_data)
	if bcrypt.check_password_hash(user[0]['password'], password):
		flash("Logged in")
		session['loggedin'] = user[0]['id']
		return redirect('/wall')
	else:
		flash("Invalid Password")
	return redirect('/')
@app.route('/message', methods= ['POST'])
def	message():
	query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
	data = {'user_id': session['loggedin'],'message': request.form['message']}
	mysql.query_db(query, data)
	return redirect('/wall')
@app.route('/comment', methods = ['POST'])
def comment():
	query = "INSERT INTO comments(message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
	data = {'user_id': session['loggedin'],'message_id': request.form['message'], 'comment': request.form['comment']}
	mysql.query_db(query, data)
	return redirect('/wall')
@app.route('/wall')
def success():
	messages = mysql.query_db("SELECT messages.id, messages.created_at, users.first_name, users.last_name, messages.message FROM messages LEFT JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC")
	for message in messages:
		comment_query = "SELECT comments.id, comments.created_at, users.first_name, users.last_name, comments.comment FROM comments LEFT JOIN users ON users.id = comments.user_id WHERE message_id = :message ORDER BY comments.created_at ASC"
		query_data = {'message':message['id']}
		comment = mysql.query_db(comment_query, query_data)
		message['all_comments']=comment
	return render_template('wall.html', all_messages = messages)
app.run(debug = True)
