from django.db import models

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.models import ModelBarProduct
from cheers.apps.base.models.base import ModelAbstractBase


class ModelBarProductRating(ModelAbstractBase):
    """
    This model store the rating  of the bar and product.
    """

    user = models.ForeignKey(ModelAccountUser, on_delete=models.CASCADE, related_name="ratings")
    product = models.ForeignKey(ModelBarProduct, on_delete=models.CASCADE, related_name="ratings")
    bar_rating = models.PositiveIntegerField(help_text="The rating of particular bar", null=True, blank=True)
    product_rating = models.PositiveIntegerField(help_text="The rating of particular product", null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)


    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_product_rating"
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the rating bar object.
        """

        return str(self.product.id)

