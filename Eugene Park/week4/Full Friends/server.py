from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friendsdb')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends_list = mysql.query_db(query)
	return render_template('index.html', friends_list = friends_list)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email']
			}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id = :friend_id"
	data = {'friend_id': id}
	single_friend = mysql.query_db(query, data)
	return render_template('edit.html', single_friend = single_friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	query = "UPDATE friends SET first_name = :edited_first_name, last_name = :edited_last_name, email = :edited_email, updated_at = NOW() WHERE id = :id"
	data = {
			'edited_first_name': request.form['first_name'],
			'edited_last_name': request.form['last_name'],
			'edited_email': request.form['email'],
			'id': id
			}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['GET', 'POST'])
def destroy(id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)