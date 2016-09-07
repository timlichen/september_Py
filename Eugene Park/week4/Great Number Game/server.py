from flask import Flask, render_template, random, session, redirect
app = Flask(__name__)

@app.before_first_request
def first_roll():
	session['roll'] = random.randrange(0,101)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/replay')
def replay():
	session['roll'] = random.randrange(0,101)
	return redirect('/')

app.run(debug=True)