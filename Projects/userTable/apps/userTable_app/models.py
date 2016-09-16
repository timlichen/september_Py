from __future__ import unicode_literals

from django.db import models

# userManger class and methods.
class userManager(models.Manager):
    # create a method that can be called through objects.
    def validatePresence(self, postData):
        # accepts postData (see **)
        # print postData['name']
        # print postData['favFood']
        # print postData['favCity']
        if len(postData['name']) > 0 and len(postData['favFood']) > 0 and len(postData['favCity']) > 0:
            return True
        else:
            return False

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=45)
    favorite_food = models.CharField(max_length=45)
    favorite_city = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # extending objects class to userManager class (see above).
    objects = userManager()
