# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadBoy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('votes', models.IntegerField()),
            ],
        ),
    ]
