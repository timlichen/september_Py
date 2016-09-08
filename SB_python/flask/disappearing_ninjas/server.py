from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def showall():
	image = 'all.jpg'
	return render_template('ninja.html', image=image)

@app.route('/ninja/<color>')
def showspecific(color):
	if color == 'blue':
		image = 'leonardo.jpg'
	elif color == 'orange':
		image = 'michelangelo.jpg'
	elif color == 'red':
		image = 'raphael.jpg'
	elif color == 'purple':
		image = 'donatello.jpg'
	else:
		image = 'notapril.jpg'
	return render_template('ninja.html', image=image)

app.run(debug=True)