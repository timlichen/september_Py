from flask import Flask, request, redirect, render_template
import unirest

app = Flask(__name__)

@app.route("/")
def index():
	response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/Ysera",
	headers= {
	"X-Mashape-Key": "cA6YALuRv9mshEOch3xgeix69eppp1W4iITjsnGkE75kNoE9ti",
	"Accept": "application/json"
	})
	cardData = response.body[0]
	return render_template("index.html", data=cardData)

@app.route("/getCard", methods=['POST'])
def getCard():
	cardURL = "https://omgvamp-hearthstone-v1.p.mashape.com/cards" + request.form['cardName']

	response = unirest.get(cardURL. headers=("X-Mashape-Key": "cA6YALuRv9mshEOch3xgeix69eppp1W4iITjsnGkE75kNoE9ti", "Accept": "application/json"))
  	

app.run(debug=True)