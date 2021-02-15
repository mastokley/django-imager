# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0003_imagerprofile_camera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='photography_type',
            field=models.CharField(choices=[('ad', 'advertising'), ('am', 'amateur'), ('bl', 'black and white'), ('co', 'color'), ('co', 'commercial'), ('cr', 'crime scene'), ('ed', 'editorial'), ('fa', 'fashion'), ('fo', 'food'), ('la', 'landscape'), ('ph', 'photojournalism'), ('po', 'portrait and wedding'), ('st', 'still life'), ('wi', 'wildlife')], default='amateur', max_length=2),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='region',
            field=models.CharField(choices=[('Af', 'Africa'), ('An', 'Antarctica'), ('As', 'Asia'), ('Au', 'Australia'), ('Eu', 'Europe'), ('No', 'North America'), ('So', 'South America')], max_length=2),
        ),
    ]
