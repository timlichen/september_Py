# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendsonfriends', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='combo',
            old_name='first_id',
            new_name='first',
        ),
        migrations.RenameField(
            model_name='combo',
            old_name='second_id',
            new_name='second',
        ),
    ]
