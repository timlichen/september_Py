import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='Secret'
@app.route('/')
def index():
	session['number'] = random.randrange(0,101)
	return render_template('index.html', result = '')
@app.route('/number', methods = ['POST'])
def number():
	if session['number'] < int(request.form['number']):
		compare = '<div class="red">Too High!</div>'
	elif session['number'] > int(request.form['number']):
		compare = '<div class = "red">Too Low!</div>'
	elif session['number'] == int(request.form['number']):
		compare = "<div class ='green'>"+ str(session["number"]) + " was the number!<br><button onclick='location.href=\"/\"'>Play Again!</button></div>"
	return render_template('index.html', result = compare)
app.run(debug = True)