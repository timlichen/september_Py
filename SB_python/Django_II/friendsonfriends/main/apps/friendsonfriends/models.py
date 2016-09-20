from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class Combo(models.Model):
	first = models.ForeignKey('User', models.DO_NOTHING, related_name = "first_friend")
	second = models.ForeignKey('User', models.DO_NOTHING, related_name = "second_friend")
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)