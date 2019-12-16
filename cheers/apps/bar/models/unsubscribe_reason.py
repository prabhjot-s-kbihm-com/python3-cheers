from django.db import models


class ModelBarUnsubscribeReason(models.Model):
    """
    This model store the reason for unsubscribe the plan.
    """

    title = models.CharField(max_length=500, help_text="reason for unsubscibe")

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_unsubscribe_reason"
        verbose_name = "Unsubscribe Reason"
        verbose_name_plural = "Unsubscribe Reasons"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the reason object.
        """

        return self.title
