# Generated by Django 2.2.1 on 2019-07-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190520_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelaccountuser',
            name='name',
        ),
        migrations.AddField(
            model_name='modelaccountuser',
            name='first_name',
            field=models.CharField(blank=True, help_text="User's first name.", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='modelaccountuser',
            name='surname',
            field=models.CharField(blank=True, help_text="User's surname.", max_length=200, null=True),
        ),
    ]
