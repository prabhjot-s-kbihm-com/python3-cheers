from rest_framework import serializers

from cheers.apps.bar.models import ModelBarTiming


class SerializerBarTiming(serializers.ModelSerializer):

    class Meta:
        model = ModelBarTiming
        fields = ('day', 'start_time', 'end_time', "is_closed")