# Generated by Django 2.2.1 on 2019-05-08 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0004_modelbarcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelbar',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bars', to='bar.ModelBarCategory'),
            preserve_default=False,
        ),
    ]
