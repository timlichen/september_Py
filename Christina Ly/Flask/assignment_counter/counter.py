from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Secret'
@app.route('/')
def index():
	try:
		session['count']+=1
	except:
		session['count']=0
	return render_template('index.html')
@app.route('/double')
def double_count():
	session['count']+=1
	return redirect('/')
@app.route('/reset')
def reset():
	session['count']=0
	return redirect('/')
app.run(debug = True)