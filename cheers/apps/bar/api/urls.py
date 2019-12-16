from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from cheers.apps.bar.api.views.bar import ViewAPIBar
from cheers.apps.bar.api.views.bar_category import ViewAPIBarCategory
from cheers.apps.bar.api.views.check_subscription_expiration import ViewAPIBarCheckSubscriptionExpire
from cheers.apps.bar.api.views.order import ViewAPIBarOrder
from cheers.apps.bar.api.views.payment import ViewAPIBarPayment
from cheers.apps.bar.api.views.plan import ViewAPIBarPlan
from cheers.apps.bar.api.views.product import ViewAPIBarProduct
from cheers.apps.bar.api.views.rating import ViewAPIBarProductRating
from cheers.apps.bar.api.views.stripe_card_list import ViewAPIBarStripeCardList
from cheers.apps.bar.api.views.unsubscribe import ViewAPIBarUnsubscribe
from cheers.apps.bar.api.views.unsubscribe_reason import ViewAPIBarUnsubscribeReason

router = routers.DefaultRouter()

# User's has signup (POST), detail (GET), update (PATCH, PUT) api's
router.register('products', ViewAPIBarProduct, base_name='products')
router.register('orders', ViewAPIBarOrder, base_name='orders')
router.register('', ViewAPIBar, base_name='bars')



urlpatterns = [


    # path('list/',
    #     ViewAPIBar.as_view(), name='lists'),

    path('category/',
        ViewAPIBarCategory.as_view(), name='category'),

    path('plans/',
        ViewAPIBarPlan.as_view(), name='plans'),

    path('payment/',
        ViewAPIBarPayment.as_view(), name='payment'),

    path('cards/',
        ViewAPIBarStripeCardList.as_view(), name='cards'),



    path('check-subscription-expiration/',
        ViewAPIBarCheckSubscriptionExpire.as_view(), name='check-subscription-expiration'),

    path('rating/',
        ViewAPIBarProductRating.as_view(), name='rating'),

    path('unsubscribe/',
        ViewAPIBarUnsubscribe.as_view(), name='unsubscribe'),

    path('reasons/',
        ViewAPIBarUnsubscribeReason.as_view(), name='reasons'),

    path('', include(router.urls)),

]
