from rest_framework import serializers

from cheers.apps.bar.models import ModelBarOrder, ModelBarSubscription, ModelBar
from django.utils.translation import ugettext_lazy as _

class SerializerBarOrder(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product_image = serializers.SerializerMethodField()
    product_bar = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    order_date = serializers.SerializerMethodField()


    class Meta:
        model = ModelBarOrder
        fields = ('bar', 'product', 'created', 'product_image', 'product_name',
                  'product_bar', 'user', 'order_date')

    def get_product_image(self, obj):
        """
        :return product image
        """
        request = self.context.get("request")
        return request.build_absolute_uri(obj.product.preview_image)

    def get_product_name(self, obj):
        """
        :return product name
        """
        return obj.product.name

    def get_product_bar(self, obj):
        """
        :return product bar name
        """
        return obj.bar.name

    def get_order_date(self, obj):
        """
        :return: order date
        """
        return obj.created.date()

    def validate(self, data):
        """
        This method check the user subscription and daily quota for drinks.
        """
        if not ModelBar.objects.filter(id=data.get('bar').id,drinks=data.get('product')).exists():
            raise serializers.ValidationError({'product': [_('This product is not realted with this bar.')]})

        try:
            ModelBarSubscription.objects.get(user=data.get('user'), active=True)
        except ModelBarSubscription.DoesNotExist:
            raise serializers.ValidationError({'user': [_('This user has no active subscription.')]})


        if  data.get('user').is_today_order_allowed:
            raise serializers.ValidationError({'order': [_('Your today quota exceeded')]})

        return  data

