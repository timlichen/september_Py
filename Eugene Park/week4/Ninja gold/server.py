from flask import Flask, render_template, redirect, request, session
from time import strftime, localtime
import random
app = Flask(__name__)
app.secret_key = 'shhh'

@app.before_first_request
def initialize():
	session['wallet'] = 0
	session['activity_log'] = ''

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money():
	time = strftime("(%Y/%m/%d %I:%M %p)", localtime())
	if request.form['building'] == 'farm':
		roll = int(random.randrange(10,21))
		session['activity_log'] += '<span class="green">Earned '+str(roll)+ ' golds from the farm! '+time+'</span><br>'
		session['wallet'] += roll
	elif request.form['building'] == 'cave':
		roll = int(random.randrange(5,11))
		session['activity_log'] += '<span class="green">Earned '+str(roll)+ ' golds from the cave! '+time+'</span><br>'
		session['wallet'] += roll
	elif request.form['building'] == 'house':
		roll = int(random.randrange(2,6))
		session['activity_log'] += '<span class="green">Earned '+str(roll)+ ' golds from the house! '+time+'</span><br>'
		session['wallet'] += roll
	elif request.form['building'] == 'casino':
		roll = int(random.randrange(0,51))
		win = int(random.randrange(0,2))
		if win:
			session['activity_log'] += '<span class="green">Entered a casino and earned '+str(roll)+ ' golds! '+time+'</span><br>'
		else:
			session['activity_log'] += '<span class="red">Entered a casino and lost '+str(roll)+ ' golds... Ouch.. '+time+'</span><br>'
			roll *= -1
		session['wallet'] += roll
	
	return redirect('/')

app.run(debug=True)