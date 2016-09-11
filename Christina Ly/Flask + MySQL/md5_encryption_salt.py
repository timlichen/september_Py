import md5
password = 'password';
encrypted_password = md5.new(password).hexdigest();
print encrypted_password;


SALT:

import os, binascii
salt = binascii.b2a_hex(os.urandom(15))

username = request.form['username']
email = request.form['email']
password = request.form['password']
salt =  binascii.b2a_hex(os.urandom(15))
encrypted_pw = md5.new(password + salt).hexdigest()
insert_query = "INSERT INTO users (username, email, password, salt, created_at, updated_at) VALUES (:username, :email, :encrypted_pw, :salt, NOW(), NOW())"
query_data = { 'username': username, 'email': email, 'encrypted_pw': encrypted_pw, 'salt': salt}
mysql.query_db(insert_query, query_data)