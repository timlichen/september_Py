# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0002_remove_user_confirm'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login_registration.User'),
        ),
    ]
