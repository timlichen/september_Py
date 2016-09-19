from __future__ import unicode_literals

from django.db import models

# class userManager(models.Manager):
# 	def validatePresence(self, postData):



class User(models.Model):
	name = models.CharField(max_length=45)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	# objects = userManager()