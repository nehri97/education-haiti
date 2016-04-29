# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20160417_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='university',
            field=models.CharField(choices=[(b'1', b'Illinois State University'), (b'2', b'Mount Holyoke College'), (b'3', b'University of Notre Dame'), (b'4', b'Columbia University'), (b'5', b'Cornell University'), (b'6', b'Ecole Polytechnique de Montreal'), (b'7', b'Georgia Tech University'), (b'8', b'Harvard University'), (b'9', b'Louisiana State University'), (b'10', b'Massachusettes Institute of Technology'), (b'11', b'McGill University'), (b'12', b'Moncton University'), (b'13', b'Southern University'), (b'14', b'Tufts University'), (b'15', b'University of Michigan'), (b'16', b'University of Pennsyvalnia'), (b'17', b'Cooper Union'), (b'18', b'St Leo University'), (b'19', b'Stony Brook University'), (b'20', b'University of Ottawa'), (b'21', b'Berea College'), (b'22', b'Massasoit CC'), (b'23', b'University of Massachusetts'), (b'24', b'University of South Florida')], default=b'No University', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='university',
            field=models.CharField(choices=[(b'1', b'Illinois State University'), (b'2', b'Mount Holyoke College'), (b'3', b'University of Notre Dame'), (b'4', b'Columbia University'), (b'5', b'Cornell University'), (b'6', b'Ecole Polytechnique de Montreal'), (b'7', b'Georgia Tech University'), (b'8', b'Harvard University'), (b'9', b'Louisiana State University'), (b'10', b'Massachusettes Institute of Technology'), (b'11', b'McGill University'), (b'12', b'Moncton University'), (b'13', b'Southern University'), (b'14', b'Tufts University'), (b'15', b'University of Michigan'), (b'16', b'University of Pennsyvalnia'), (b'17', b'Cooper Union'), (b'18', b'St Leo University'), (b'19', b'Stony Brook University'), (b'20', b'University of Ottawa'), (b'21', b'Berea College'), (b'22', b'Massasoit CC'), (b'23', b'University of Massachusetts'), (b'24', b'University of South Florida')], default=b'No University', max_length=255),
        ),
    ]
