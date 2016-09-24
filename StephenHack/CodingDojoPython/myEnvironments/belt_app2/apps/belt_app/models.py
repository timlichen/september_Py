from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from ..login_reg_app.models import User
# Create your models here.

class AppUser(models.Model):
	user = models.ForeignKey(User)
	email = models.CharField(max_length=45)
	reviews = models.TextField()
	ratings = models.CharField(max_length=45)

class Author(models.Model):
	author_name = models.CharField(max_length=45)
	title = models.CharField(max_length=45)
