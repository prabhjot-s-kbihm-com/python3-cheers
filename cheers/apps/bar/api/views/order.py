from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from cheers.apps.bar.api.serializers.order import SerializerBarOrder
from cheers.apps.bar.models import ModelBarOrder


class ViewAPIBarOrder(ModelViewSet):
    """
    This class is used for bar order
    """

    serializer_class = SerializerBarOrder
    model = ModelBarOrder

    def get_queryset(self):
        """
        Return the order by user and ordered by latest created date.
        """

        user = self.request.user
        return self.model.objects.filter(user=user).order_by("-created")







