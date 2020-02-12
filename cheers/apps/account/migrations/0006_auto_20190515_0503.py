# Generated by Django 2.2.1 on 2019-05-15 05:03

import cheers.apps.account.models.user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190515_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelaccountuser',
            name='avatar',
            field=models.ImageField(blank=True, help_text="User's avatar.", max_length=500, null=True, upload_to=cheers.apps.account.models.user.get_upload_path),
        ),
    ]