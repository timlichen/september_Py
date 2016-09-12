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

   if len(request.form['name']) < 1:
      flag = True
      flash("Name cannot be empty")

   if len(request.form['comment']) < 1:
      flag = True
      flash("Comment cannot be empty")

   if len(request.form['comment']) > 120:
      flag = True
      flash("Comment can't be more than 120 characters")
   
   if not flag:
      return render_template('results.html', name=name, location=location, language=language, comment=comment)
   else:
      return redirect('/')
app.run(debug=True)