# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-18 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
