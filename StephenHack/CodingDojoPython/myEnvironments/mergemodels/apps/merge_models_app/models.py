from __future__ import unicode_literals

from django.db import models

from ..first_app.models import Course 
from ..login_reg_app.models import User

class Merge(models.Model):
	course = models.ForeignKey(Course)
	user = models.ForeignKey(User)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

# Create your models here.
