from __future__ import unicode_literals
from django.db import models
from ..login_reg_app.models import User

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	review = models.TextField()
	rating = models.CharField(max_length=1)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)