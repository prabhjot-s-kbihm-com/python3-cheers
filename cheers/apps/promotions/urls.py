
from django.urls.conf import path
from cheers.apps.promotions.views import ViewPromotions

urlpatterns = [
   path('promotions/', ViewPromotions.as_view(),
         name="index")
]

