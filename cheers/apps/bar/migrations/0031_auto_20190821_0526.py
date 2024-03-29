# Generated by Django 2.2.1 on 2019-08-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0030_modelbarproduct_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelbarproduct',
            name='image_height',
            field=models.PositiveSmallIntegerField(default=550),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='modelbarproduct',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', help_text='Logo of the bar', null=True, upload_to='bar/product/'),
        ),
    ]
