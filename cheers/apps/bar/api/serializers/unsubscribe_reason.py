from rest_framework import serializers

from cheers.apps.bar.models.unsubscribe_reason import ModelBarUnsubscribeReason

class SerializerBarUnsubscribeReason(serializers.ModelSerializer):

    class Meta:
        model = ModelBarUnsubscribeReason
        fields = ('id', 'title')

