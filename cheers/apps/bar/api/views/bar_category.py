from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from cheers.apps.bar.api.serializers.bar_category import SerializerBarCategory
from cheers.apps.bar.models import ModelBarCategory
from cheers.apps.base.api.serializers.country import SerializerBaseCountry
from cheers.apps.base.models import ModelBaseCountry


class ViewAPIBarCategory(ListAPIView):
    """
    This class handle the category of bar.
    """
    model = ModelBarCategory
    serializer_class = SerializerBarCategory
    queryset = model.objects.all()
    pagination_class = None