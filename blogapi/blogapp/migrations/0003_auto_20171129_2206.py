# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20171128_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]