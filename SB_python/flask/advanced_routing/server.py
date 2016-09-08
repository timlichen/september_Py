from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "Gotit"

@app.route('/users/<username>')
def index(username):
	return render_template('index.html', username=username)

app.run(debug=True)