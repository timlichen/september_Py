from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'Secret'
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/ninja')
def allninja():
	allninjas = []
	allninjas.append('img/leonardo.jpg')
	allninjas.append('img/michelangelo.jpg')
	allninjas.append('img/raphael.jpg')
	allninjas.append('img/donatello.jpg')
	return render_template('ninja.html', allninjas = allninjas)
@app.route('/ninja/<ninja_color>')
def color(ninja_color):
	color = []
	if ninja_color == 'red':
		color.append('img/raphael.jpg')
	elif ninja_color == 'orange':
		color.append('img/michelangelo.jpg')
	elif ninja_color== 'purple':
		color.append('img/donatello.jpg')
	elif ninja_color == 'blue':
		color.append('img/leonardo.jpg')
	else:
		color.append('img/notapril.jpg')
	return render_template('ninja.html', allninjas = color)
app.run(debug = True)
