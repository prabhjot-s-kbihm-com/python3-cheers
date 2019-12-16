from rest_framework import serializers

from cheers.apps.bar.models import ModelBarProductRating


class SerializerBarProductRating(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ModelBarProductRating
        fields = ('product', 'created', 'bar_rating', 'product_rating',
                  'feedback', 'user')