"""
                            API URL's
"""

from django.urls.conf import include
from django.urls.conf import path

urlpatterns = [
    # path('base/', include(('cheers.apps.base.api.urls', 'base'), namespace='base')),
    #
    path('account/',
         include(('cheers.apps.account.api.urls', 'account'), namespace='account')),

    path('base/',
         include(('cheers.apps.base.api.urls', 'base'), namespace='base')),

    path('bar/',
         include(('cheers.apps.bar.api.urls', 'bar'), namespace='bar')),

]