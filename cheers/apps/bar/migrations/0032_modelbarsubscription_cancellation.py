# Generated by Django 2.2.1 on 2019-09-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0031_auto_20190821_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelbarsubscription',
            name='cancellation',
            field=models.BooleanField(default=False, help_text='when user unsubscribe it will be true'),
        ),
    ]
