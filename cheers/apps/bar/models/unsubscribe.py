from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.models.plan import ModelBarPlan
from cheers.apps.bar.models.unsubscribe_reason import ModelBarUnsubscribeReason
from cheers.apps.base.models.base import ModelAbstractBase


class ModelBarUnsubscribe(ModelAbstractBase):
    """
    This model store the data of bar subscription.
    """

    user = models.ForeignKey(ModelAccountUser, related_name="cancelled_subscriptions",
                              on_delete=models.CASCADE, help_text="User related to subscription")

    plan = models.ForeignKey(ModelBarPlan, on_delete=models.CASCADE, related_name="cancelled_subscriptions")
    reason = models.ForeignKey(ModelBarUnsubscribeReason, on_delete=models.CASCADE,
                               related_name="cancelled_subscriptions")

    comment = models.TextField()

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_plan_cancelled_subscription"
        verbose_name = "Cancelled Subscription"
        verbose_name_plural = "Cancelled Subscriptions"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the  unsubscriptions plan object.
        """

        return "Plan:{0}, Cancelled by: {1}".format(self.plan.title, self.user.email)