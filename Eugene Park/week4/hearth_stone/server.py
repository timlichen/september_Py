from flask import Flask, request, redirect, render_template, flash
import unirest
app = Flask(__name__)
app.secret_key = 'secrete'

@app.route('/')
def index():
	response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/Ysera",
 	 headers={
    "X-Mashape-Key": "BWYuyVWCE5mshB9rQVK9ppcyLp1Wp1oAfpZjsnJ8znQQxkeyNg",
    "Accept": "application/json"
  	})
  	cardData = response.body[0]
	return render_template('index.html', data=cardData)
@app.route('/getCard', methods=['POST'])
def getCard():
	cardURL = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/"+request.form['cardName']
	response = unirest.get(cardURL,
 	 headers={
    "X-Mashape-Key": "BWYuyVWCE5mshB9rQVK9ppcyLp1Wp1oAfpZjsnJ8znQQxkeyNg",
    "Accept": "application/json"
  	})
	if len(request.form['cardName']) < 2:
		flash('Card name must be at least 2 characters')
		return redirect('/')
  	if not type(response.body) == dict:
  		cardData = response.body[0]
  		return render_template('index.html', data=cardData)
  	else:
  		flash("This card does not exist")
  		return redirect('/')
	
app.run(debug=True)