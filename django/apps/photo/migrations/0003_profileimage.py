
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20150512_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('photo.imagefile',),
        ),
    ]
