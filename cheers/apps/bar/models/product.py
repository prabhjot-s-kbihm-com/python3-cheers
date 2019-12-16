from django.db import models

# image, name, price, id, description,  bar_id,
from cheers.apps.account.models import ModelAccountUser


class ModelBarProduct(models.Model):
    """
    This model store the product of the bar.
    """

    name = models.CharField(max_length=500, help_text="Name of the Product")
    image_height = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to="bar/product/", null=True, blank=True,
                              help_text="Logo of the bar", height_field='image_height')
    owner = models.ForeignKey(ModelAccountUser, on_delete=models.CASCADE, related_name="products")
    price = models.FloatField(null=True, blank=True)
    description = models.TextField()
    is_default = models.BooleanField(default=False, help_text="show products which are deafult show to every user")

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the product object.
        """

        return self.name

    @property
    def preview_image(self):
        return self.image.url if self.image else '/static/images/drink.jpg'
