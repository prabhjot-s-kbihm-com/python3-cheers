from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from cheers.apps.bar.models import ModelBar, ModelBarTiming, ModelBarCategory, ModelBarProduct, ModelBarProductRating, \
    ModelBarSubscription, ModelBarPlan, ModelBarOrder, ModelBarUnsubscribeReason, ModelBarUnsubscribe


class TimingInline(admin.StackedInline):
    model = ModelBarTiming
    extra = 0


@admin.register(ModelBar)
class AdminBar(OSMGeoAdmin):
    default_zoom = 30
    inlines = [TimingInline]

# @admin.register(ModelBarTiming)
# class AdminBarTiming(admin.ModelAdmin):
#     pass

@admin.register(ModelBarCategory)
class AdminBarCategory(admin.ModelAdmin):
    pass

@admin.register(ModelBarProduct)
class AdminBarProduct(admin.ModelAdmin):
    pass

@admin.register(ModelBarProductRating)
class AdminBarProductRating(admin.ModelAdmin):
    pass

@admin.register(ModelBarPlan)
class AdminBarPlan(admin.ModelAdmin):
    pass

@admin.register(ModelBarSubscription)
class AdminBarSubscription(admin.ModelAdmin):
    pass

@admin.register(ModelBarOrder)
class AdminBarOrder(admin.ModelAdmin):
    pass

@admin.register(ModelBarUnsubscribeReason)
class AdminBarUnsubscribeReason(admin.ModelAdmin):
    pass

@admin.register(ModelBarUnsubscribe)
class AdminBarBarUnsubscribe(admin.ModelAdmin):
    pass