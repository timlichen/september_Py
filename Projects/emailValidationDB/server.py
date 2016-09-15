from  flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "golden_bangkok"
mysql = MySQLConnector(app, 'emails')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validateEmail", methods=['POST'])
def validator():
    flag = False
    if len(request.form['email']) == 0:
        flag = True
        flash("Email field cannot be blank.")
    if not EMAIL_REGEX.match(request.form['email']):
        flag = True
        flash("Email is not valid.")
    if flag:
        return redirect("/")
    else:
        # variable to hold post/form data
        email = request.form['email']
        print email
        # Our mySQL query goes here.
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        # created a dict for email.
        session['email'] = email
        data = { "email": email}
        if mysql.query_db(query, data):
            print "Sucessfully saved to database."
        return redirect("/success")

@app.route("/success")
def success():
    query = "SELECT * from emails"
    emails = mysql.query_db(query)
    return render_template("success.html", emails = emails)

app.run(debug=True)
