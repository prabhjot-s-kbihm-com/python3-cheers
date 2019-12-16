from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.models import ModelBarPlan
from django.utils.translation import ugettext_lazy as _


class SerializerBarPayment(serializers.Serializer):

    plan = serializers.PrimaryKeyRelatedField(queryset=ModelBarPlan.objects.all())
    stripe_token = serializers.CharField(max_length=200, required=False)
    card_token = serializers.CharField(max_length=200, required=False)
    referral_code  = serializers.CharField(max_length=200, required=False)
    is_saved = serializers.BooleanField(default=False)

    def validate(self, data):
        """
        This method check the user subscription and daily quota for drinks.
        """

        referral_code = data.get("referral_code", '')
        plan = ModelBarPlan.objects.get(duration=1)
        if referral_code:
            try:
                referral_user = ModelAccountUser.objects.get(referral_code=referral_code)
                if referral_user == self.context.get("request").user:
                    raise serializers.ValidationError({'referral_code': [_("you can't use your own referral code ")]})
                if not referral_user.referral_status:
                    try:
                        subscription = referral_user.subscription
                        subscription.expiration += relativedelta(months=1)
                        subscription.save()
                    except AttributeError:
                        plan.subscribe(referral_user)
                    referral_user.referral_status = True
                    referral_user.save()

            except ModelAccountUser.DoesNotExist:
                raise serializers.ValidationError({'referral_code': [_('This code is not valid try another')]})
        return data







