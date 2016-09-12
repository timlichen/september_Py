from flask import Flask, render_template, request, redirect, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

app = Flask(__name__)

app.secret_key = 'key'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
   print "Submitted Info"
   flag = False

   email = request.form['email']
   first_name = request.form['first_name']
   last_name = request.form['last_name']
   password = request.form['password']
   confirm_password = request.form['confirm_password']   

   if len(request.form['email']) < 1:
      flag = True
      flash("Name cannot be empty")
   elif not EMAIL_REGEX.match(request.form['email']):
      flag = True
      flash("Invalid Email Address")

   if len(request.form['first_name']) < 1:
      flag = True
      flash("first_name cannot be empty")
   elif request.form['first_name'].isalpha() == False:
      flag = True
      flash("Characters must be alphabetic")

   if len(request.form['last_name']) < 1:
      flag = True
      flash("last_name cannot be empty")
   elif request.form['last_name'].isalpha() == False:
      flag = True
      flash("Characters must be alphabetic")

   if len(request.form['password']) < 1:
      flag = True
      flash("password cannot be empty")
   elif (request.form['password'] != request.form['confirm_password']):
      flag = True
      flash("password and confirm_password do not match")
   elif not PASSWORD_REGEX.match(request.form['password']):
      flag = True
      flash("Password must be at least 8 characters and contain 1 number and 1 uppercase letter")

   if len(request.form['confirm_password']) < 1:
      flag = True
      flash("confirm_password cannot be empty")
   
   if not flag:
      return render_template('results.html', email=email, first_name=first_name, last_name=last_name, password=password, confirm_password=confirm_password)
   else:
      return redirect('/')
app.run(debug=True)