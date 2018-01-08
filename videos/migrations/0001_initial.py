# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fileDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('filetype', models.CharField(choices=[('video', 'Video'), ('img', 'Image')], max_length=10)),
                ('play_from', models.DateField()),
                ('play_Till', models.DateField()),
                ('file_path', models.FileField(upload_to='')),
            ],
        ),
    ]
