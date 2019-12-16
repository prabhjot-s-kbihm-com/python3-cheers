from rest_framework import serializers
from datetime import datetime
from cheers.apps.bar.models import ModelBarUnsubscribe, ModelBarSubscription
from django.utils.translation import ugettext_lazy as _


class SerializerBarUnsubscribe(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ModelBarUnsubscribe
        fields = ('id', 'user', 'plan', 'reason', "comment")


    def validate(self, data):

        try:
            subscription = ModelBarSubscription.objects.get(user=data.get('user'))
            subscription.cancellation = True
            subscription.save()
        except ModelBarSubscription.DoesNotExist:
            raise serializers.ValidationError({'user': [_('This user has no active subscription.')]})

        return data