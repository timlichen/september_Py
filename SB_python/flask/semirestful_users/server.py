from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "name"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users')
def allusers():
	return render_template('users.html')

@app.route('/users/<id>'):
def oneuser(id):
	return render_template('user.html')

@app.route('/users/new'):
def newuser():
	return render_template('add.html')

@app.route('/users/<id>/edit'):
def edituser(id):
	return render_template('edit.html')

@app.route('/users/<id>/delete'):
def delete(id):
	return redirect('/users')