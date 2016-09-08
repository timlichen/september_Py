from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "name"

@app.before_first_request
def first_roll():
	session['roll'] = int(random.randrange(0,101))
	session['new'] = True

@app.route('/')
def index():
	if session['new']:
		return render_template('index.html')
	else:
		if session["guess"] < session['roll']:
			return render_template('index_low.html')
		elif session["guess"] > session['roll']:
			return render_template('index_high.html')
		else:
			return render_template('index_right.html')


@app.route('/guess', methods=['POST'])
def guess():
	session['new'] = False
	session["guess"] = int(request.form['user_guess'])
	return redirect('/')

@app.route('/replay')
def replay():
	session['roll'] = random.randrange(0,101)
	session['new'] = True
	return redirect('/')

app.run(debug=True)