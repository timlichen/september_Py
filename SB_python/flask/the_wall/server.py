from flask import Flask, redirect, request, render_template, session
from connection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app=Flask(__name__)
app.secret_key = "Got it"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def checkLogin():
	password = request.form['password']
	storage = mysql.query_db("SELECT * FROM users WHERE email = :email LIMIT 1", {'email' : request.form['email']})
	if storage == []:
		return redirect('/')
	else:
		if bcrypt.check_password_hash(storage[0]['password'], password):
			session['userID'] = storage[0]['id']
		else:
			session['userID'] = "WRONG"
	# sinistermessages = mysql.query_db("SELECT * FROM messages JOIN users ON messages.users_id = users.id")
	# sinistermessages = mysql.query_db("SELECT * FROM comments JOIN users ON comments.users_id = users.id")
	messages = mysql.query_db("SELECT users.first_name, users.last_name, messages.id, messages.created_at FROM messages JOIN users ON messages.users_id = users.id")
	comments = mysql.query_db("SELECT * FROM comments JOIN users ON comments.users_id = users.id")
	return render_template('wall.html', messages = messages, comments = comments)

@app.route('/register', methods=['POST'])
def register():
	password = request.form['password']
	isoguard = bcrypt.generate_password_hash(password)

	mysql.query_db("INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())", {'first_name' : request.form['first_name'], 'last_name' : request.form['last_name'], 'email': request.form['email'], 'password': isoguard})
	session['userID'] = mysql.query_db("SELECT id FROM users WHERE email = :email", {'email' : request.form['email']})[0]['id']
	messages = mysql.query_db("SELECT users.first_name, users.last_name, messages.id, messages.created_at FROM messages JOIN users ON messages.users_id = users.id")
	comments = mysql.query_db("SELECT * FROM comments JOIN users ON comments.users_id = users.id")
	return render_template('wall.html', messages = messages, comments = comments)

@app.route('/<id>/new_message', methods=['POST'])
def newMessage(id):

	mysql.query_db("INSERT INTO messages (users_id, message, created_at, updated_at) VALUES (:id, :message, NOW(), NOW())", {'id' : id, 'message' : request.form['message']})
	messages = mysql.query_db("SELECT users.first_name, users.last_name, messages.id, messages.created_at FROM messages JOIN users ON messages.users_id = users.id")
	comments = mysql.query_db("SELECT * FROM comments JOIN users ON comments.users_id = users.id")
	return render_template('wall.html', messages = messages, comments = comments)

@app.route('/comment/<mid>', methods=['POST'])
def newComment(mid):
	print int(mid)
	mysql.query_db("INSERT INTO comments (messages_id, users_id, comment, created_at, updated_at) VALUES (:messageid, :userid, :comment, NOW(), NOW())", {'messageid' : int(mid), 'userid' : session['userID'], 'comment' : request.form['comment']})
	messages = mysql.query_db("SELECT users.first_name, users.last_name, messages.id, messages.created_at FROM messages JOIN users ON messages.users_id = users.id")
	comments = mysql.query_db("SELECT * FROM comments JOIN users ON comments.users_id = users.id")
	return render_template('wall.html', messages = messages, comments = comments)

@app.route('/logoff')
def logoff():
	return redirect('/')

app.run(debug=True)
