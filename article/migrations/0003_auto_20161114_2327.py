# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20161106_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Текс коментаря'),
        ),
    ]
