from django.db import models
from django.utils.translation import ugettext_lazy as _

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.base.models.base import ModelAbstractBase
from cheers.apps.base.models.coupon import ModelBaseCoupon


class ModelBaseCouponUser(ModelAbstractBase):
    coupon = models.ForeignKey(ModelBaseCoupon, related_name='users',
                               on_delete=models.CASCADE)

    user = models.ForeignKey(ModelAccountUser, verbose_name=_("User"),
                             null=True, blank=True, on_delete=models.CASCADE, related_name='users')

    redeemed_at = models.DateTimeField(_("Redeemed at"), blank=True, null=True)

    class Meta:
        db_table = "base_coupon_user"
        verbose_name = "Coupon User"
        verbose_name_plural = "Coupon Users"

    def __str__(self):
        return str(self.user)
