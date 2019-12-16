from rest_framework import serializers

from cheers.apps.bar.models import ModelBarTiming, ModelBarPlan
from cheers.apps.base.models import ModelBaseCoupon


class SerializerBarPlan(serializers.ModelSerializer):

    # price = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()
    percentage_value = serializers.SerializerMethodField()

    class Meta:
        model = ModelBarPlan
        fields = ('id', 'title', 'price', 'discounted_price',  'description', "duration", "currency", "percentage_value")


    def get_discounted_price(self, obj):
        request = self.context.get("request")
        price = obj.discount(request.user)
        return price

    # def get_price(self, obj):
    #     return obj.price * obj.duration

    def get_percentage_value(self, obj):
        request = self.context.get("request")
        value = obj.get_percentage_value(request.user)
        return value
