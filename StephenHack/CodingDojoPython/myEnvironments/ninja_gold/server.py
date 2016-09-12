from flask import Flask, render_template, request, redirect, session
import random
import time

localtime = time.asctime( time.localtime(time.time()) )

app = Flask(__name__)

app.secret_key = 'key'

@app.before_first_request
def before():
   session['gold'] = 0
   session['log'] = " "

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():

   if request.form['building'] == 'farm':
      temp = random.randrange(10, 21)
      farm_string = "Earned " + str(temp) + "gold from the farm!" + str(localtime)
      session['gold'] += temp
      session['log'] += farm_string

   elif request.form['building'] == 'cave':
      temp = random.randrange(5, 11)
      cave_string = "Earned " + str(temp) + "gold from the farm!" + str(localtime)
      session['gold'] += temp
      session['log'] += cave_string

   elif request.form['building'] == 'house':
      temp = random.randrange(2,6)
      house_string = "Earned " + str(temp) + "gold from the farm!" + str(localtime)
      session['gold'] += random.randrange(2, 6)
      session['log'] += house_string

   elif request.form['building'] == 'casino':
      temp = random.randrange(0, 51)
      if random.randrange(0, 2) == 0:
         casino_string = "Earned " + str(temp) + "gold from the farm!" + str(localtime)
         session['gold'] += temp
         session['log'] += casino_string
      else:
         casino_string = "Lost " + str(temp) + "gold from the farm!" + str(localtime)
         session['gold'] -= temp
         session['log'] += casino_string

   return redirect('/')

app.run(debug=True)