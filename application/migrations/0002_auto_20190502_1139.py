# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
