from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from cheers.apps.bar.api.serializers.plan import SerializerBarPlan
from cheers.apps.bar.models import ModelBarCategory, ModelBarPlan


class ViewAPIBarPlan(ListAPIView):
    """
    This class handle the Plan of bar.
    """
    model = ModelBarPlan
    serializer_class = SerializerBarPlan
    queryset = model.objects.filter(is_active=True, default=True)
    pagination_class = None