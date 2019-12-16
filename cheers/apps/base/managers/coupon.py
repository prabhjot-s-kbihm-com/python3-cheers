from django.db import models
from django.db import IntegrityError
from django.utils import timezone


class CouponManager(models.Manager):
    def create_coupon(self, type, value, users=[], plan=None, valid_until=None, prefix="", campaign=None,
                      user_limit=None):

        from cheers.apps.base.models.coupon import ModelBaseCoupon
        coupon = self.create(
            value=value,
            code=ModelBaseCoupon.generate_code(prefix),
            type=type,
            plan=plan,
            valid_until=valid_until,
            campaign=campaign,
        )
        if user_limit is not None:  # otherwise use default value of model
            coupon.user_limit = user_limit
        try:
            coupon.save()
        except IntegrityError:
            # Try again with other code
            coupon = ModelBaseCoupon.objects.create_coupon(type, value, users, plan, valid_until, prefix, campaign)

        if not isinstance(users, list):
            users = [users]

        for user in users:
            if user:
                from cheers.apps.base.models.coupon_user import ModelBaseCouponUser
                ModelBaseCouponUser(user=user, coupon=coupon).save()
        return coupon

    def create_coupons(self, quantity, type, value, valid_until=None, prefix="", campaign=None):
        coupons = []
        for i in range(quantity):
            coupons.append(self.create_coupon(type, value, None, valid_until, prefix, campaign))
        return coupons

    def used(self):
        return self.exclude(users__redeemed_at__isnull=True)

    def unused(self):
        return self.filter(users__redeemed_at__isnull=True)

    def expired(self):
        return self.filter(valid_until__lt=timezone.now())
