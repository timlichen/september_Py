from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	info = [request.form['name'], request.form['location'], request.form['language'], request.form['comment']]
	return render_template('result.html', info=info)

app.run(debug=True)