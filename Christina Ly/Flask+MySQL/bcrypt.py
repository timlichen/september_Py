from flask import Flask, request, render_template
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'my_database_here')
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/create_user', methods=['POST'])
def create_user():
	email = request.form['email']
	username = request.form['username']
	password = request.form['password']
 	pw_hash = bcrypt.generate_password_hash(password)
	insert_query = "INSERT INTO users (email, username, pw_hash, created_at) VALUES (:email, :username, :pw_hash, NOW())"
	query_data = { 'email': email, 'username': username, 'password': pw_hash }
	mysql.query_db(insert_query, query_data)

CHECK PASSWORD:
unencryptedinput = "password" #variable from form
pw_hash = bcrypt.generate_password_hash(password)
bcrypt.check_password_hash(pw_hash, unencryptedinput)

EXAMPLE:
@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	query_data = { 'email': email }
	user = mysql.query_db(user_query, query_data) # user will be returned in a list
	if bcrypt.check_password_hash(user[0]['pw_hash'], password):
	# login user
	else:
	# set flash error message and redirect to login page