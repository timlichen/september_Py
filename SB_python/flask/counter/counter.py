from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "name"

@app.before_first_request
def before_request():
	session['count'] = 0

@app.route('/')
def index():
	session['count'] += 1
	return render_template('index.html')

@app.route('/one')
def test():
	session['count'] += 2
	return redirect('/')

@app.route('/two')
def test1():
	session['count'] = 0
	return redirect('/')

app.run(debug=True)