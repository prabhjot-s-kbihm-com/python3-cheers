from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from cheers.apps.bar.api.serializers.unsubscribe_reason import SerializerBarUnsubscribeReason
from cheers.apps.bar.models.unsubscribe_reason import ModelBarUnsubscribeReason


class ViewAPIBarUnsubscribeReason(ListAPIView):
    """
    This class handle the reasons of cancelled subscriptions
    """
    model = ModelBarUnsubscribeReason
    serializer_class = SerializerBarUnsubscribeReason
    queryset = model.objects.all()
    pagination_class = None

