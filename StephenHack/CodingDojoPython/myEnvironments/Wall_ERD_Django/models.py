from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
	first_name = models.CharField(max_length=30)
 	last_name = models.CharField(max_length=30)
 	email = models.textfield()
 	password = models.CharField(max_length=30)
 	created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class messages(models.Model):
	user_id = models.ForeignKey(users)
 	message= models.textfield()
 	created_at = models.DateTimeField(auto_now_add = True)
 	updated_at = models.DateTimeField(auto_now = True)

class comments(models.Model):
	message_id = models.ForeignKey(messages)
	user_id = models.ForeignKey(users)
	created_at = models.DateTimeField(auto_now_add = True)
 	updated_at = models.DateTimeField(auto_now = True)