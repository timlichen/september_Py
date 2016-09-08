from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "name"

@app.before_first_request
def run_server():
    session['counter'] = 0

@app.route('/')
def index():
   # if session['counter'] < 1:
   #    session['counter'] = 1
   # else:
   session['counter'] += 1


   return render_template('index.html') 
@app.route('/two')
def two():
   session['counter'] += 1
   return redirect('/')

@app.route('/three')
def three():
   session['counter'] = 0
   return redirect('/')
app.run(debug=True)