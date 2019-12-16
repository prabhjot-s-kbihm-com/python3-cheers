from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from cheers.apps.bar.models import ModelBarCategory


class SerializerBarCategory(serializers.ModelSerializer):
    icon = Base64ImageField(required=False)

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelBarCategory
        fields = ('id', 'name', "icon")

