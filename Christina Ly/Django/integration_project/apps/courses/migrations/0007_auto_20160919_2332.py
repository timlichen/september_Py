# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20160919_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='user',
            field=models.ManyToManyField(to='login_registration.User'),
        ),
    ]