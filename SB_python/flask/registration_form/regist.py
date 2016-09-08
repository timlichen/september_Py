from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "wo!"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/reg', methods=['POST'])
def validate():
	done = True
	hasUpper = False
	hasDigit = False

	for i in range(0, len(request.form['password'])):
		if request.form['password'][i].isupper():
			hasUpper = True
		if request.form['password'][i].isdigit():
			hasDigit = True

	if not hasDigit:
		flash('PASSWORD MUST CONTAIN AT LEAST ONE NUMBER')
		done = False
	if not hasUpper:
		flash('PASSWORD MUST CONTAIN AT LEAST ONE UPPER CASE LETTER')
		done = False
	if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['passwordcheck']) < 1:
		flash('ALL FORMS MUST BE COMPLETED')
		done = False
	if (not request.form['first_name'].isalpha()) or (not request.form['last_name'].isalpha()):
		flash('NAMES MUST ONLY BE LETTERS')
		done = False
	if len(request.form['password']) < 8:
		flash('PASSWORD MUST EXCEED 8 CHARACTERS')
		done = False
	if not request.form['password'] == request.form['passwordcheck']:
		flash('PASSWORD CHECK INCORRECT')
		done = False
	if not EMAIL_REGEX.match(request.form['email']):
		flash('INVALID EMAIL')
		done = False
	if done:
		flash('Good job!')
	return redirect('/')

app.run(debug=True)