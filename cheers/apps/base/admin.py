from django.contrib import admin

from cheers.apps.base.models import ModelBaseCountry, ModelBaseCoupon, ModelBaseCampaign, ModelBaseCouponUser, \
    ModelBaseFAQ


@admin.register(ModelBaseCoupon)
class AdminBaseCoupon(admin.ModelAdmin):
    pass


@admin.register(ModelBaseCampaign)
class AdminBaseCampaign(admin.ModelAdmin):
    pass


@admin.register(ModelBaseCouponUser)
class AdminBaseCouponUser(admin.ModelAdmin):
    pass


@admin.register(ModelBaseCountry)
class AdminBaseCountry(admin.ModelAdmin):
    pass


@admin.register(ModelBaseFAQ)
class AdminBaseFAQ(admin.ModelAdmin):
    pass
