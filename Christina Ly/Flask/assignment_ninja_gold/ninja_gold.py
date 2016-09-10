import random
import time
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='Secret'
@app.before_first_request
def init():
	session['gold'] = 0
	session['activities'] = ''
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/process_money', methods =['POST'])
def money():
	if request.form['building'] == 'farm':
		earn = random.randrange(10,21)
		session['gold'] += earn
		session['activities'] = '<span class ="green">Earned '+str(earn)+" golds from the farm ("+time.strftime("%Y-%m-%d %I:%M %p")+") <br>" + session['activities']+'</span>'
	elif request.form['building'] == 'cave':
		earn = random.randrange(5,11)
		session['gold'] += earn
		session['activities']= '<span class ="green">Earned '+str(earn)+" golds from the cave ("+time.strftime("%Y-%m-%d %I:%M %p")+") <br>" + session['activities']+'</span>'
	elif request.form['building'] == 'house':
		earn = random.randrange(2,6)
		session['gold'] += earn
		session['activities']= '<span class ="green">Earned '+str(earn)+" golds from the house ("+time.strftime("%Y-%m-%d %I:%M %p")+") <br>" + session['activities']+'</span>'
	elif request.form['building'] == 'casino':
		earn = random.randrange(-50,51)
		if earn < 0:
			session['gold'] += earn
			session['activities']= '<span class ="red">Entered a casino and lost '+str(earn)+" golds... Ouch.. ("+time.strftime("%Y-%m-%d %I:%M %p")+") <br>" + session['activities']+'</span>'
		if earn > 0:
			session['gold'] += earn
			session['activities']= '<span class ="green">Entered a casino and won '+str(earn)+" golds ("+time.strftime("%Y-%m-%d %I:%M %p")+") <br>" + session['activities']+'</span>'
	return redirect('/')
app.run(debug = True)