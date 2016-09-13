from flask import Flask, render_template, redirect, request
from connection import MySQLConnection
app = Flask(__name__)
app.secret_key = "yep"

mysql = MySQLConnection(app, 'full_friends2')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	name = request.form['name']
	mysql.query_db("INSERT INTO friends (name, created_at, updated_at) VALUES (:name, NOW(), NOW())", {"name" : name}):
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	unique = mysql.query_db("SELECT * FROM friends WHERE id = " + id)
	print unique[0]['id']
	return render_template('friends.html', unique = unique)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	prac = str(id).replace("<", "")
	prac = prac.replace(">", "")
	mysql.query_db("UPDATE friends SET name = " + "'" + request.form['name_edit'] + "'" + ", updated_at = NOW() WHERE id = " + prac + ";")
	return redirect('/')

@app.route('/friends/<id>/delete')
def delete(id):
	mysql.query_db("DELETE FROM friends WHERE id = " + id)
	return redirect('/')

app.run(debug=True)