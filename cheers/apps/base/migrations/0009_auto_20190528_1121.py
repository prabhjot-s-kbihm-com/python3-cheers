# Generated by Django 2.2.1 on 2019-05-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_modelbasecoupon_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelbasecountry',
            name='name',
            field=models.CharField(help_text='Name of the country', max_length=200, unique=True),
        ),
    ]
