from django import forms

from cheers.apps.base.models.coupon import ModelBaseCoupon
from cheers.apps.base.models.coupon_user import ModelBaseCouponUser
from django.utils.translation import ugettext_lazy as _


class CouponForm(forms.Form):
    code = forms.CharField(label=_("Coupon code"))

    def __init__(self, *args, **kwargs):

        self.user = None
        self.types = None

        if 'user' in kwargs:
            self.user = kwargs['user']
            del kwargs['user']

        if 'types' in kwargs:
            self.types = kwargs['types']
            del kwargs['types']

        super(CouponForm, self).__init__(*args, **kwargs)

    def clean_code(self):
        code = self.cleaned_data['code']

        try:
            coupon = ModelBaseCoupon.objects.get(code=code)
        except ModelBaseCoupon.DoesNotExist:
            raise forms.ValidationError(_("This code is not valid."))


        self.coupon = coupon # set the coupon property so anyone calling this form can have coupon object

        if self.user is None and coupon.user_limit is not 1:
            # coupons with can be used only once can be used without tracking the user, otherwise there is no chance
            # of excluding an unknown user from multiple usages.
            raise forms.ValidationError(_(
                "The server must provide an user to this form to allow you to use this code. Maybe you need to sign in?"
            ))

        if coupon.type == 'subscription' and self.user.subscription:
            raise forms.ValidationError(_("Sorry can't use this coupon now. You already has an active subscription."))

        if coupon.type == "percentage":
            if ModelBaseCoupon.objects.used().filter(users__user=self.user).exists():
                raise forms.ValidationError(_("This code has already been used by your account."))

        if coupon.is_redeemed:
            raise forms.ValidationError(_("This code has already been used."))

        try:  # check if there is a user bound coupon existing
            user_coupon = coupon.users.get(user=self.user, redeemed_at=None)

            if user_coupon.redeemed_at is not None:
                raise forms.ValidationError(_("This code has already been used by your account."))

        except ModelBaseCouponUser.DoesNotExist:
            if coupon.user_limit is not 0:  # zero means no limit of user count
                # only user bound coupons left and you don't have one
                if coupon.user_limit is coupon.users.filter(user__isnull=False).count():
                    raise forms.ValidationError(_("This code is not valid for your account."))
                if coupon.user_limit is coupon.users.filter(redeemed_at__isnull=False).count():  # all coupons redeemed
                    raise forms.ValidationError(_("This code has already been used."))

        if self.types is not None and coupon.type not in self.types:
            raise forms.ValidationError(_("This code is not meant to be used here."))

        if coupon.expired():
            raise forms.ValidationError(_("This code is expired."))


        return code
