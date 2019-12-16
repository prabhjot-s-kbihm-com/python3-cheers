from rest_framework.generics import ListAPIView
from cheers.apps.base.api.serializers.faq import SerializerBaseFAQ
from cheers.apps.base.models import  ModelBaseFAQ


class ViewAPIBaseFAQ(ListAPIView):
    """
    This class handle the FAQ's.
    """
    model = ModelBaseFAQ
    serializer_class = SerializerBaseFAQ
    queryset = model.objects.all()
    pagination_class = None