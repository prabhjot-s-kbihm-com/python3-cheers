"""
                        BASE API URL'S
"""

from django.urls.conf import path
from cheers.apps.base.api.views.country import ViewAPIBaseCountry
from cheers.apps.base.api.views.faq import ViewAPIBaseFAQ
from cheers.apps.base.api.views.redeem_coupon import ViewAPIBaseRedeemCoupon

urlpatterns = [
    path('country/', ViewAPIBaseCountry.as_view(), name="country"),
    path('redeem-coupon/', ViewAPIBaseRedeemCoupon.as_view(), name="redeem-coupon"),
    path('faq/', ViewAPIBaseFAQ.as_view(), name="faq"),

]
