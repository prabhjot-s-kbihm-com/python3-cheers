# Generated by Django 2.2.1 on 2019-05-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0002_modelbar_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelbar',
            name='logo',
            field=models.ImageField(blank=True, help_text='Logo of the bar', null=True, upload_to='bar/'),
        ),
    ]
