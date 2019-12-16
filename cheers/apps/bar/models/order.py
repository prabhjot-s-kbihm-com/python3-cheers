from django.db import models

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.models import ModelBarProduct, ModelBar
from cheers.apps.base.models.base import ModelAbstractBase
from datetime import datetime

class ModelBarOrder(ModelAbstractBase):
    """
    This model store the order of the user.
    """

    user = models.ForeignKey(ModelAccountUser, related_name="orders",
                              on_delete=models.CASCADE, help_text="User which is order a product")

    bar = models.ForeignKey(ModelBar, related_name="orders", on_delete=models.CASCADE)

    product = models.ForeignKey(ModelBarProduct, related_name="orders", on_delete=models.CASCADE)



    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the product order object.
        """
        return "{0} ordered {1} at the {2}".format(self.user.email, self.product.name, self.product.bars.name)
