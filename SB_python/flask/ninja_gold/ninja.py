from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "yeah"

@app.before_first_request
def givegold():
	session['gold'] = 0
	session['activities'] = ""

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	print session['activities']
	if request.form['building'] == 'farm':
		coins = round(random.randrange(10, 21))
		session['gold'] += coins
		session['activities'] = "Just got " + str(coins)
	elif request.form['building'] == 'cave':
		coins = round(random.randrange(1, 11))
		session['gold'] += coins
		session['activities'] = "Just got " + str(coins)
	elif request.form['building'] == 'house':
		coins = round(random.randrange(1, 3))
		session['gold'] += coins
		session['activities'] = "Just got " + str(coins)
	elif request.form['building'] == 'casino':
		coins = round(random.randrange(-50, 50))
		session['gold'] += coins
		session['activities'] = "Just got " + str(coins)
	else:
		pass
	return redirect('/')

app.run(debug=True)