# Generated by Django 2.2.1 on 2019-05-15 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0011_modelbarunsubscribe_modelbarunsubscribereason'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_modelbasecampaign_modelbasecoupon_modelbasecouponuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelbasecoupon',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='created_coupons'),
        ),
        migrations.AddField(
            model_name='modelbasecoupon',
            name='plan',
            field=models.ForeignKey(blank=True, help_text='Select plan if this coupon is subscription based', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='bar.ModelBarPlan', verbose_name='Subscription Plan'),
        ),
    ]
