import logging

from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone

from cheers.apps.base.models.base import ModelAbstractBase

logger = logging.getLogger(__name__)


class ModelBarPlan(ModelAbstractBase):
    """
    This model store the data of bar plans.
    """

    CURRENCIES_TYPES = (('usd', 'USD'), ("eur", 'EUR'))
    INTERVAL_CHOICES = (('day', 'Day'), ('month', 'Month'), ('year', 'Year'))

    title = models.CharField(max_length=255, help_text="Title of the plan")

    price = models.FloatField(help_text="Specify one time price of the price (per interval). "
                                                  "If plan is monthly provide 1 month price, if it's "
                                                  "yearly provide 1 year or 12 month price")

    description = models.TextField(null=True, blank=True)

    duration = models.PositiveIntegerField(help_text="Duration")

    interval = models.CharField(max_length=100, choices=INTERVAL_CHOICES,
                                default=INTERVAL_CHOICES[1][0])

    currency = models.CharField(choices=CURRENCIES_TYPES, max_length=20,
                                help_text="In which currency you want to pay.")

    default = models.BooleanField(default=False,
                                  help_text="Check if this plan are the main "
                                            "plans for the application")

    is_active = models.BooleanField(default=True,
                                    help_text="Admin toggle to display/hide "
                                              "the plan from the user")

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_plan"
        verbose_name = "Plan"
        verbose_name_plural = "Plans"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the bar plan object.
        """

        return self.title

    @property
    def calculate_expiration_from_today(self):
        """
        Expiration datetime is duration*month or duration*year or days from payment datetime
        :return:
        """
        if self.interval == 'month':
            return timezone.now() + relativedelta(months=self.duration)
        elif self.interval == 'year':
            return timezone.now() + relativedelta(months=self.duration * 12)
        elif self.interval == 'day':
            return timezone.now() + relativedelta(days=self.duration)

    def subscribe(self, user, coupon=None, transaction_details={}, language=None):
        from cheers.apps.bar.models import ModelBarSubscription

        subscription_data = {"user": user,
                             "plan": self,
                             "expiration": self.calculate_expiration_from_today,
                             "transaction_details": transaction_details,
                             "coupon": coupon,
                             "active": True
                             }

        if user.cancel_subscription:
            old_subscription = user.cancel_subscription
            old_subscription.active = False
            old_subscription.save()

        subscription = ModelBarSubscription.objects.create(**subscription_data)
        logger.info(('{0} subscription Created for user {1}'.format(self.title, user)))

        # send payment acknowledgement email to user.
        logger.info(
            ('sending subscription email to the user {0} for subscription {1}'.format(user, self.title)))

        subscription.send_activation_subscription_email(language=language)

    def discount(self, user):

        from cheers.apps.base.models import ModelBaseCoupon
        try:
            coupon = ModelBaseCoupon.objects.get(plan=self, type="percentage")
            coupon_user = coupon.users.filter(user=user, redeemed_at__isnull=False).exists()
            if coupon_user:
                actual_price = self.price * self.duration
                calculated_price = actual_price * float(coupon.value) / 100
                discounted_price = actual_price - calculated_price
                self.coupon_value = coupon.value
                print("original price, discount, discounted price", self.price, coupon.value, discounted_price)
                return discounted_price
        except:
            return None

    def get_percentage_value(self, user):
        discount_value = self.discount(user)
        if discount_value:
            return "{0}%".format(self.coupon_value)
