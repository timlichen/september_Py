from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def create_user():
	print "yes"
	return render_template('results.html', name = request.form['name'], location = request.form['location'], language = request.form['lang'], comments = request.form['comments'])

app.run(debug=True)