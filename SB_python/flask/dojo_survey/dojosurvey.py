from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "nothing"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def create_user():
	if len(request.form['name']) < 1 and len(request.form['comments']) < 1:
		flash("Name cannot be empty!")
		flash("Comments cannot be empty!")

	elif len(request.form['comments']) < 1:
		flash("Comments cannot be empty!")

	elif len(request.form['comments']) > 120:
		flash("Comments cannot exceed 120 characters!")

	elif len(request.form['name']) < 1:
		flash("Name cannot be empty!")

	else:
		name = request.form['name']
		comments = request.form['comments']
	return render_template('results.html', name = name, location = request.form['location'], language = request.form['lang'], comments = comments)

app.run(debug=True)