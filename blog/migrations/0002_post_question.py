# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='question',
            field=models.CharField(choices=[('keking', 'kek'), ('loling', 'lol'), ('hehing', 'heh'), ('lmaoing', 'lmao')], default='keking', max_length=4),
        ),
    ]
