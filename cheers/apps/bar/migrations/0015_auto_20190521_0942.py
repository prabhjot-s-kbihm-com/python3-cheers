# Generated by Django 2.2.1 on 2019-05-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0014_modelbar_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelbar',
            name='latitude',
            field=models.DecimalField(decimal_places=6, help_text='Latitude of bar address', max_digits=15),
        ),
        migrations.AlterField(
            model_name='modelbar',
            name='longitude',
            field=models.DecimalField(decimal_places=6, help_text='Longitude of bar address', max_digits=15),
        ),
    ]