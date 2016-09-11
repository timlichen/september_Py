from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key ="Secret"
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/result', methods = ['POST'])
def result():
	if len(request.form['name']) <1:
		flash("Name cannot be empty!")
		return redirect('/')
	elif len(request.form['comment']) >121 or len(request.form['comment']) <1:
		flash("Character count must be between 1 and 120")
		return redirect('/') 
	name = request.form['name']
	dojo_location = request.form['dojo_location']
	favorite_lang = request.form['favorite_lang']
	comment = request.form['comment']
	return render_template('result.html', name = name, dojo_location = dojo_location, favorite_lang= favorite_lang, comment= comment)
app.run(debug=True)


