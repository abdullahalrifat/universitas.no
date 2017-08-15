# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-15 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0023_auto_20170815_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='publication_status',
            field=models.IntegerField(choices=[(0, 'Draft'), (3, 'To Journalist'), (4, 'To Sub Editor'), (5, 'To Editor'), (6, 'Ready for newsdesk'), (9, 'Ready to publish on website'), (10, 'Published on website'), (11, 'Published, but hidden from search engines'), (15, 'Will not be published'), (100, 'Used as template for new articles'), (500, 'Technical error')], default=0, help_text='publication status.', verbose_name='status'),
        ),
    ]
