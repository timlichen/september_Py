from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'I_am_reusing_this'
mysql = MySQLConnector(app, 'the_wall')
bcrypt = Bcrypt(app)

@app.before_first_request
def run_server():
	session['id'] = 0
	session['name'] = ''

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
		session['id'] = mysql.query_db('SELECT id FROM users WHERE email = :email', {'email': email})[0]['id']
		return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	query = "SELECT * FROM users WHERE email LIKE :email LIMIT 1"
	data = {'email': email}
	user = mysql.query_db(query, data)
	if bcrypt.check_password_hash(user[0]['password'], password):
		session['id'] = user[0]['id']
		session['name'] = str(user[0]['first_name']) +" "+ str(user[0]['last_name'])
		return redirect('/success')
	else:
		flash('Unable to login')
		return redirect('/')

@app.route('/log_out')
def log_out():
	session['name'] = ''
	session['id'] = 0
	return redirect('/')

@app.route('/post_msg', methods=['POST'])
def post_msg():
	query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES(:id, :message, now(), now())"
	data = {'id': session['id'], 'message': request.form['message']}
	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/post_cmt/<msg_id>', methods=['POST'])
def post_cmt(msg_id):
	query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES(:msg_id, :id, :comment, now(), now())"
	data = {'msg_id': msg_id ,'id': session['id'], 'comment': request.form['comment']}
	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/success')
def success():
	messages = mysql.query_db("SELECT messages.id, messages.created_at, messages.message, users.first_name, users.last_name FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.id DESC")
	comments = mysql.query_db("SELECT comments.id, comments.message_id, comments.user_id, comments.comment, comments.created_at, users.first_name, users.last_name FROM comments JOIN users ON comments.user_id = users.id ORDER BY comments.id ASC")
	return render_template('wall.html', messages = messages, comments = comments)

app.run(debug=True)