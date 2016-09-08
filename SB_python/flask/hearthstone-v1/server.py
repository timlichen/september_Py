from flask import Flask, render_template, request, redirect, flash
import unirest
app = Flask(__name__)
app.secret_key = "NO"
@app.route('/')
def index():
	response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/Ysera", headers={"X-Mashape-Key": "Ey2xkix2w0mshHGGdtAkDgzGkVSpp103WJnjsnjDIHVXtZ3Buq", "Accept": "application/json"})
	print response.body[0]
	return render_template('index.html', data=response.body[0])

@app.route('/card', methods=['POST'])
def getcard():
	cardinput = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/" + request.form['cardname']
	response = unirest.get(cardinput, headers={"X-Mashape-Key": "Ey2xkix2w0mshHGGdtAkDgzGkVSpp103WJnjsnjDIHVXtZ3Buq", "Accept": "application/json"})
	if not response.body['error']:
		carddata = response.body[0]
		return render_template('index.html', data=carddata)
	else:
		flash("Wrong character name!")
		return redirect('/')

app.run(debug=True)