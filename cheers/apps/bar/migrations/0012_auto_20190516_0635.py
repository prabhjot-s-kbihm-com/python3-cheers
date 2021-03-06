# Generated by Django 2.2.1 on 2019-05-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0011_modelbarunsubscribe_modelbarunsubscribereason'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelbarplan',
            name='default',
            field=models.BooleanField(default=False, help_text='Check if this plan are the main plans for the application'),
        ),
        migrations.AddField(
            model_name='modelbarplan',
            name='interval',
            field=models.CharField(choices=[('day', 'Day'), ('month', 'Month'), ('year', 'Year')], default='month', max_length=100),
        ),
        migrations.AlterField(
            model_name='modelbarplan',
            name='duration',
            field=models.PositiveIntegerField(help_text='Duration'),
        ),
    ]
