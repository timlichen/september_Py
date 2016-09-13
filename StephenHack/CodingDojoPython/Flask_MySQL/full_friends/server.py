from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'key'

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {'first_name': request.form['first_name'], 'last_name':  request.form['last_name'],'occupation': request.form['occupation']}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend>/edit', methods=['POST'])
def edit(friend):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend}
    friends = mysql.query_db(query, data)
    print friends
    return render_template('edit.html', friends=friends[0])

@app.route('/friends/<friend>/update', methods=['POST'])
def update(friend):
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, occupation=:occupation WHERE id=:id"
    data = {'first_name': request.form['first_name'], 
            'last_name': request.form['last_name'], 
            'occupation':request.form['occupation'],
            'id': friend}
    mysql.query_db(query, data)
    return redirect('/')  

@app.route('/friends/<friend>/delete', methods=['POST'])
def delete(friend):
    query = "DELETE FROM friends WHERE id=:id"
    data = {'id': friend}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)