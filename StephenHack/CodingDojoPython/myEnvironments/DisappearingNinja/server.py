from flask import Flask, render_template, request, redirect
app = Flask(__name__)

ninja_displayed = ''

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninjas')
def ninja():
	return render_template("ninja.html")

@app.route('/ninjas/<ninja>')
def show_ninja(ninja):
	if ninja == 'blue':
		ninja_displayed = 'leonardo.jpg'
	elif ninja == 'red':
		ninja_displayed = "{{ url_for('static', filename='IMG/raphael.jpg') }}"
	elif ninja == 'orange':
		ninja_displayed = "michelangelo.jpg"
	elif ninja == 'purple':
		ninja_displayed = "{{ url_for('static', filename='IMG/michelangelo.jpg') }}"

  	return render_template("ninja.html", ninja=ninja_displayed)

app.run(debug=True)