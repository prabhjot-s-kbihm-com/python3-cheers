# Generated by Django 2.2.1 on 2019-05-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20190516_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBaseFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Question about the product', max_length=500)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': "FAQ's",
                'db_table': 'base_faq',
            },
        ),
    ]
