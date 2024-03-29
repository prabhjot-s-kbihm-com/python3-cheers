# Generated by Django 2.2.1 on 2019-05-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0021_auto_20190528_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelbar',
            name='latitude',
            field=models.DecimalField(decimal_places=10, help_text='Latitude of bar address', max_digits=15),
        ),
        migrations.AlterField(
            model_name='modelbar',
            name='longitude',
            field=models.DecimalField(decimal_places=10, help_text='Longitude of bar address', max_digits=15),
        ),
    ]
