from rest_framework import serializers

from cheers.apps.base.models import  ModelBaseFAQ


class SerializerBaseFAQ(serializers.ModelSerializer):
    """
    Handle the data related with FAQ's
    """

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelBaseFAQ
        fields = ('id', 'question', 'answer')
