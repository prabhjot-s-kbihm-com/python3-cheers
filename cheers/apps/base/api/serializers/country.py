from rest_framework import serializers

from cheers.apps.base.models import ModelBaseCountry


class SerializerBaseCountry(serializers.ModelSerializer):
    """
    Validates and serializes the data of country.
    """

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelBaseCountry
        fields = ('id', 'name')
