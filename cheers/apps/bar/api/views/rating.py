from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from cheers.apps.bar.api.serializers.rating import SerializerBarProductRating


class ViewAPIBarProductRating(CreateAPIView):
    """
    This class is used for product rating
    """

    serializer_class = SerializerBarProductRating

