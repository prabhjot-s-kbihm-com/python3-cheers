from django.contrib.postgres.fields.jsonb import JSONField
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import render_to_string

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.models.plan import ModelBarPlan
from cheers.apps.base.models import ModelBaseCoupon
from cheers.apps.base.models.base import ModelAbstractBase
from cheers.settings import DEFAULT_FROM_EMAIL


class ModelBarSubscription(ModelAbstractBase):
    """
    This model store the data of bar subscription.
    """

    user = models.ForeignKey(ModelAccountUser, related_name="subscriptions",
                             on_delete=models.SET_NULL, null=True,
                             help_text="User related to subscription")

    plan = models.ForeignKey(ModelBarPlan, on_delete=models.SET_NULL,
                             null=True, related_name="subscriptions")

    expiration = models.DateTimeField()

    cancellation = models.BooleanField(default=False, help_text="when user unsubscribe it will be true")

    coupon = models.ForeignKey(ModelBaseCoupon, null=True, blank=True,
                               on_delete=models.SET_NULL,
                               help_text="Coupon attached to the subscription.")

    active = models.BooleanField(default=False,
                                 help_text="The active subscription of the user")

    transaction_details = JSONField(default=dict, null=True, blank=True)

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_subscription"
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the bar subscription object.
        """
        if self.user:
            return "Plan:{0}, Taken by: {1}".format(self.plan.title, self.user.email)
        else:
            return self.plan

    # ---------------------------------------------------------------------------
    # send_verification_email
    # ---------------------------------------------------------------------------
    def send_activation_subscription_email(self, language=None):
        """
        Sends the activation subscription mail to the user.
        """

        subject = "Your Cheers World Subscription has been Activated"
        context_data = {"user": self.user,
                        "plan": self.plan,
                        "language":language
                        }

        html_template_path = "emails/subscription-email.html"
        text_template_path = 'emails/subscription-email.txt'

        html_content = render_to_string(html_template_path, context_data)

        msg = EmailMultiAlternatives(subject, text_template_path, DEFAULT_FROM_EMAIL, [self.user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
