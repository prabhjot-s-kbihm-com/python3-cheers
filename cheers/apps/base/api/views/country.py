from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from cheers.apps.base.api.serializers.country import SerializerBaseCountry
from cheers.apps.base.models import ModelBaseCountry


class ViewAPIBaseCountry(ListAPIView):
    """
    This class handle the country.
    """
    model = ModelBaseCountry
    serializer_class = SerializerBaseCountry
    queryset = model.objects.filter(is_enabled=True)
    pagination_class = None