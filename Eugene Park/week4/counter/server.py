from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "name"

@app.before_first_request
def run_server():
	session['counter'] = 0

@app.route('/')
def index():
	session['counter'] += 1
	return render_template('index.html')

@app.route('/two')
def plus_two():
	session['counter'] += 1
	return redirect('/')

@app.route('/reset')
def reset():
	session['counter'] = 0
	return redirect('/')

app.run(debug=True)