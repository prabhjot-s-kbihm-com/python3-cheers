from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from cheers.apps.bar.models import ModelBarProduct


class SerializerBarProduct(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelBarProduct
        fields = ('id', 'name', "image", "price", "description", "owner")