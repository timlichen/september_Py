from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjas():
	style_file = "all_ninja.css"
	return render_template('ninjas.html', style_file = style_file)

@app.route('/ninja/<ninja_color>')
def ninja(ninja_color):
	if ninja_color == 'blue':
		style_file = "blue.css"
	elif ninja_color == 'orange':
		style_file = "orange.css"
	elif ninja_color == 'red':
		style_file = "red.css"
	elif ninja_color == 'purple':
		style_file = "purple.css"
	else:
		style_file = "megan.css"
	return render_template('ninjas.html', style_file = style_file)

app.run(debug=True)