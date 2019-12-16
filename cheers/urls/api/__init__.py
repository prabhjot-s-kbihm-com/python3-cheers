from django.urls.conf import include
from django.urls.conf import path

# versioned includes
urlpatterns = [
    path('v0.1/', include(('cheers.urls.api.v0_1', 'v0_1'), namespace='v0_1')),
]