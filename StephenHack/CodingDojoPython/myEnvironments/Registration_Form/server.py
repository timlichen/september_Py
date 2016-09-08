from flask import Flask, render_template, request, redirect, flash

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

   if len(request.form['first_name']) < 1:
      flag = True
      flash("first_name cannot be empty")

   if len(request.form['last_name']) < 1:
      flag = True
      flash("last_name cannot be empty")

   if len(request.form['password']) < 1:
      flag = True
      flash("password cannot be empty")

   if len(request.form['confirm_password']) < 1:
      flag = True
      flash("confirm_password cannot be empty")
   
   if not flag:
      return render_template('results.html', email=email, first_name=first_name, last_name=last_name, password=password, confirm_password=confirm_password)
   else:
      return redirect('/')
app.run(debug=True)