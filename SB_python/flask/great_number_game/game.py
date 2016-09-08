from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'now'

@app.before_first_request
def before():
	session['magic'] = random.randrange(0, 101)

@app.route('/')
def index():
	afile = 'style.css'
	return render_template('index.html', afile=afile)

@app.route('/a', methods=['POST'])
def guess():
	print int(request.form['guess']), session['magic']
	if int(request.form['guess']) == session['magic']:
		session['error'] = "The number was, in fact, " + str(session['magic']) + ". You win! Play again!"
		session['magic'] = random.randrange(0, 101)
		session['color'] = 'green'
	elif int(request.form['guess']) < session['magic']:
		session['error'] = 'Too low'
		session['color'] = 'blue'
	elif int(request.form['guess']) > session['magic']:
		session['error'] = 'Too high'
		session['color'] = 'yellow'
	return redirect('/')

app.run(debug=True)