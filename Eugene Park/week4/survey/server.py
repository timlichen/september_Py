from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
app.secret_key = 'Victoria\'s'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	if len(request.form['name']) < 1 or len(request.form['comment']) < 1:
		flash("Name or the comment field cannot be empty!")
		return redirect('/')
	if len(request.form['comment']) > 120:
		flash("Comment cannot be longer than 120 characters!")
		return redirect('/')
	info = [request.form['name'], request.form['location'], request.form['language'], request.form['comment']]
	return render_template('result.html', info=info)

app.run(debug=True)