from django.contrib.gis.geos import Point
from drf_extra_fields.fields import Base64ImageField
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from cheers.apps.bar.models import ModelBar


class SerializerBar(serializers.ModelSerializer):
    """
    This serializer handle the bar data.
    """
    logo = Base64ImageField(required=False)
    category_name = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()

    class Meta:
        model = ModelBar
        fields = ('id', 'name', 'address', "latitude", "longitude",
                  "description", "phone", "email", "logo", "category_name", "bar_photography",
                  "distance", 'bar_timings')

    def get_category_name(self, obj):
        """
        :return Category name
        """
        # return "juice"
        return [category.name for category in obj.bar_category.all()]


    def get_distance(self, obj):
        """

        :param obj:
        :return:
        """
        user_lat = self.context.get('user_lat')
        user_lng = self.context.get('user_lng')

        if user_lat and user_lng:

            p1 = Point(float(user_lat), float(user_lng))
            p2 = Point(float(obj.latitude), float(obj.longitude))
            distance = p1.distance(p2) *100
            return "{:.1f}km".format(distance) # keep upto 1 decimal places
        return 0
