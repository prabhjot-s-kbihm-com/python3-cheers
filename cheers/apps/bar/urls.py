"""
                        BAR URL'S
"""


from django.urls.conf import path
from django.urls.conf import re_path

from cheers.apps.bar.views.bar_add_new import ViewBarAdd
from cheers.apps.bar.views.bar_detail import ViewBarDetail
from cheers.apps.bar.views.bar_drinks import ViewBarDrinks
from cheers.apps.bar.views.bar_owner_add import ViewBarOwnerAdd
from cheers.apps.bar.views.bar_owners import ViewBarOwners
from cheers.apps.bar.views.bar_update import ViewBarUpdate
from cheers.apps.bar.views.drink_add import ViewBarAddDrink
from cheers.apps.bar.views.drink_detail import ViewBarDrinkDetail
from cheers.apps.bar.views.drink_update import ViewBarDrinkUpdate
from cheers.apps.bar.views.list import ViewBarList
from cheers.apps.bar.views.products import ViewBarProducts
from cheers.apps.bar.views.publish import ViewBarPublish

urlpatterns = [
    #Bar urls
    path('add-bar/', ViewBarAdd.as_view(), name="add-bar"),
    path('list/', ViewBarList.as_view(), name="list"),
    path('<int:pk>/detail/', ViewBarDetail.as_view(), name='detail'),
    path('<int:pk>/update/', ViewBarUpdate.as_view(), name='update'),
    path('<int:pk>/drinks/', ViewBarDrinks.as_view(), name='drinks'),
    path('owners/', ViewBarOwners.as_view(), name='owners'),
    path('add-bar-owner/', ViewBarOwnerAdd.as_view(), name='add-bar-owner'),
 

    #Drinks urls
    path('add-drink/', ViewBarAddDrink.as_view(), name='add-drink'),
    path('drinks/', ViewBarProducts.as_view(), name='products'),
    path('<int:pk>/drink-detail/', ViewBarDrinkDetail.as_view(), name='drink-detail'),
    path('<int:pk>/drink-update/', ViewBarDrinkUpdate.as_view(), name='drink-update'),
    path('<int:pk>/publish/', ViewBarPublish.as_view(), name='publish'),





]
