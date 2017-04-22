# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 20:17
from __future__ import unicode_literals

import apps.photo.cropping.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0008_auto_20170214_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefile',
            name='crop_box',
            field=apps.photo.cropping.models.BoxField(
                default=apps.photo.cropping.models.default_crop_box,
                help_text='How this image has been cropped.',
                null=True,
                verbose_name='crop box'
            ),
        ),
    ]
