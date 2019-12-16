from django import forms

from cheers.apps.base.models.campaign import Campaign
from cheers.settings import COUPON_TYPES
from django.utils.translation import ugettext_lazy as _


class CouponGenerationForm(forms.Form):

    quantity = forms.IntegerField(label=_("Quantity"))

    value = forms.IntegerField(label=_("Value"))

    type = forms.ChoiceField(label=_("Type"), choices=COUPON_TYPES)

    valid_until = forms.SplitDateTimeField(
        label=_("Valid until"), required=False,
        help_text=_("Leave empty for coupons that never expire")
    )

    prefix = forms.CharField(label="Prefix", required=False)

    campaign = forms.ModelChoiceField(
        label=_("Campaign"), queryset=Campaign.objects.all(), required=False
    )

