# Generated by Django 2.2.1 on 2019-05-14 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bar', '0010_modelbarorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBarUnsubscribeReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='reason for unsubscibe', max_length=500)),
            ],
            options={
                'verbose_name': 'Unsubscribe Reason',
                'verbose_name_plural': 'Unsubscribe Reasons',
                'db_table': 'bar_unsubscribe_reason',
            },
        ),
        migrations.CreateModel(
            name='ModelBarUnsubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this entry was created in the system')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time when the table data was last updated in the system')),
                ('comment', models.TextField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancelled_subscriptions', to='bar.ModelBarPlan')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancelled_subscriptions', to='bar.ModelBarUnsubscribeReason')),
                ('user', models.ForeignKey(help_text='User related to subscription', on_delete=django.db.models.deletion.CASCADE, related_name='cancelled_subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cancelled Subscription',
                'verbose_name_plural': 'Cancelled Subscriptions',
                'db_table': 'bar_plan_cancelled_subscription',
            },
        ),
    ]