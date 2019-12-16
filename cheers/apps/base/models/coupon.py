from django.utils import timezone

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cheers.apps.base.managers.coupon import CouponManager
from cheers.apps.base.models.base import ModelAbstractBase
from cheers.settings import COUPONS_SEGMENTED_CODES, COUPONS_SEGMENT_SEPARATOR, COUPONS_CODE_CHARS, \
    COUPONS_SEGMENT_LENGTH, COUPONS_CODE_LENGTH, COUPON_TYPES


class ModelBaseCoupon(ModelAbstractBase):
    value = models.IntegerField(_("Value"), default=0,
                                help_text=_("Arbitrary coupon value, not required when creating subscription coupons"))

    code = models.CharField(
        _("Code"), max_length=30, unique=True, blank=True,
        help_text=_("Leaving this field empty will generate a random code."))

    type = models.CharField(_("Type"), max_length=20, choices=COUPON_TYPES)

    user_limit = models.PositiveIntegerField(_("User limit"), default=1)

    created_by = models.ForeignKey('account.ModelAccountUser', related_name="created_coupons",
                                   verbose_name=_("Created By"),
                                   null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    description = models.TextField(null=True, blank=True)

    valid_until = models.DateTimeField(
        _("Valid until"), blank=True, null=True,
        help_text=_("Leave empty for coupons that never expire"))

    plan = models.ForeignKey('bar.ModelBarPlan', verbose_name=_("Subscription Plan"),
                             blank=True, null=True, related_name="coupons",
                             on_delete=models.CASCADE,
                             help_text="Select plan if this coupon is subscription based")

    bar = models.ForeignKey('bar.ModelBar', verbose_name=_("Bar"),
                            blank=True, null=True, related_name="coupons",
                            on_delete=models.CASCADE,
                            help_text="Select bar if this coupon is restricted to particular bar")

    campaign = models.ForeignKey('ModelBaseCampaign', verbose_name=_("Campaign"),
                                 blank=True, null=True, related_name='coupons',
                                 on_delete=models.CASCADE)

    objects = CouponManager()

    class Meta:
        ordering = ['created_at']
        db_table = "base_coupon"
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ModelBaseCoupon.generate_code()

        super(ModelBaseCoupon, self).save(*args, **kwargs)

    def expired(self):
        return self.valid_until is not None and self.valid_until < timezone.now()

    @property
    def is_redeemed(self):
        """ Returns true is a coupon is redeemed (completely for all users) otherwise returns false. """
        return self.users.filter(
            redeemed_at__isnull=False
        ).count() >= self.user_limit and self.user_limit is not 0

    @property
    def redeemed_at(self):
        try:
            return self.users.filter(redeemed_at__isnull=False).order_by('redeemed_at').last().redeemed_at
        except self.users.through.DoesNotExist:
            return None

    @classmethod
    def generate_code(cls, prefix="", segmented=COUPONS_SEGMENTED_CODES):

        import random
        code = "".join(random.choice(COUPONS_CODE_CHARS) for i in range(COUPONS_CODE_LENGTH))

        if segmented:
            code = COUPONS_SEGMENT_SEPARATOR.join(
                [code[i:i + COUPONS_SEGMENT_LENGTH] for i in range(0, len(code), COUPONS_SEGMENT_LENGTH)])
            return prefix + code
        else:
            return prefix + code


    @classmethod
    def redeem_code(cls, user, code):
        from cheers.apps.base.models.coupon_user import ModelBaseCouponUser  # keep this import here
        from cheers.apps.base.forms.coupon import CouponForm

        form = CouponForm({'code': code}, user=user)
        errors = {'code': ','.join(form.errors['code'])} if form.errors else None

        coupon_user = None

        if form.is_valid():
            # try:
            #     coupon_user = self.users.get(user=user)
            # except ModelBaseCouponUser.DoesNotExist:

            # silently fix unbound or null'd coupon users
            try:
                coupon_user = form.coupon.users.get(redeemed_at__isnull=True)
            except ModelBaseCouponUser.DoesNotExist:
                coupon_user = ModelBaseCouponUser(coupon=form.coupon, user=user)

            coupon_user.redeemed_at = timezone.now()
            coupon_user.save()

            if form.coupon.type == "subscription":
                form.coupon.plan.subscribe(user, coupon=form.coupon)

            if form.coupon.type == "percentage":
                print(form.coupon.plan.price)

        return coupon_user, errors
