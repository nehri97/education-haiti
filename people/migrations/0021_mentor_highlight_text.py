# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-01 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0020_auto_20171201_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='highlight_text',
            field=models.TextField(default='Highlight Story'),
        ),
    ]