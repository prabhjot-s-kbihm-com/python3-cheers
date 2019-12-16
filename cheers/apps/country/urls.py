from django.urls.conf import path
from django.urls.conf import re_path

from cheers.apps.country import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:country_id>/edit', views.edit, name='edit'),
]
