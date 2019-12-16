from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cheers.apps.bar.api.serializers.product import SerializerBarProduct
from cheers.apps.bar.models import ModelBarProduct, ModelBar


class ViewAPIBarProduct(ModelViewSet):
    """
    This class handle the product of the bar
    """

    model = ModelBarProduct
    serializer_class = SerializerBarProduct
    http_method_names = ['get', 'delete', 'post']


    def get_queryset(self):
        """
        This method return the products according to bar or all products.
        """

        bar_id = self.request.GET.get("bar_id")

        if bar_id:
            try:
                return ModelBar.objects.get(id=bar_id).drinks.all()
            except ModelBar.DoesNotExist:
                return []

        return self.model.objects.all()



