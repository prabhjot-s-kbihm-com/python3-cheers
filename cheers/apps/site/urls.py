"""
                        SITE URL'S
"""


from django.urls.conf import path

from cheers.apps.site.views.term_condition import ViewSiteTermCondition

urlpatterns = [

    path('term-condition/', ViewSiteTermCondition.as_view(),
         name="term-condition"),


]
