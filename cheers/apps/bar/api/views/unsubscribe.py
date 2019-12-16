from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from cheers.apps.bar.api.serializers.unsubscribe import SerializerBarUnsubscribe
from cheers.apps.bar.api.serializers.unsubscribe_reason import SerializerBarUnsubscribeReason
from cheers.apps.bar.models import ModelBarUnsubscribe
from cheers.apps.bar.models.unsubscribe_reason import ModelBarUnsubscribeReason


class ViewAPIBarUnsubscribe(CreateAPIView):
    """
    This class handle the  cancelled subscriptions of the user.
    """
    model = ModelBarUnsubscribe
    serializer_class = SerializerBarUnsubscribe
    queryset = model.objects.all()
    pagination_class = None