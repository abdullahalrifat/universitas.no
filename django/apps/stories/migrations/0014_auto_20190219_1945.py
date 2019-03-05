# Generated by Django 2.1.5 on 2019-02-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0013_auto_20181117_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='comment_field',
            field=models.CharField(choices=[('facebook', 'facebook'), ('disqus', 'disqus'), ('off', 'off')], default='off', help_text='Enable comment field', max_length=16, verbose_name='Comment Field'),
        ),
    ]