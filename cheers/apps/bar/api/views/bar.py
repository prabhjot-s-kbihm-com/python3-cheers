from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cheers.apps.bar.api.serializers.bar import SerializerBar
from cheers.apps.bar.models import ModelBar


class ViewAPIBar(ModelViewSet):
    """
    This class handle the list of bars
    """
    serializer_class = SerializerBar
    model = ModelBar

    def get_serializer_context(self):

        lat = self.request.GET.get('user_lat')
        lng = self.request.GET.get('user_lng')

        context = super(ViewAPIBar, self).get_serializer_context()
        if lat and lng:
            context['user_lat'] = lat
            context['user_lng'] = lng

        return context

    def get_queryset(self):
        """
        Return the data according to filter or all bars.
        """

        filters = {}
        query = self.request.GET.get("q", '')
        country = self.request.GET.get("country_id")
        category = self.request.GET.get("category_id")
        lat = self.request.GET.get('user_lat')
        lng = self.request.GET.get('user_lng')

        radius = self.request.GET.get("radius")

        queryset = self.model.objects.all()

        if country:
            filters['country__id'] = country

        if category:
            filters['bar_category__id'] = category.lower()

        if radius and lat and lng:
            ref_location = Point(float(lng), float(lat))
            print(radius)
            filters['location__distance_lt'] = (ref_location, D(km=radius))

        if filters:
            queryset = queryset.filter(Q(name__icontains=query) | Q(address__icontains=query), **filters)
            if radius and lat and lng:
                queryset = queryset.annotate(distance=Distance("location", ref_location)) \
                    .order_by('distance')

        return queryset



