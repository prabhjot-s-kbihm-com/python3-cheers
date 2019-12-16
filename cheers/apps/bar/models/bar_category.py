from django.db import models

class ModelBarCategory(models.Model):
    """
    Store the Category of bar.
    """

    name = models.CharField(max_length=200, help_text="Name of the category")
    icon = models.ImageField(upload_to="bar/category/",
                             null=True, blank=True,
                             help_text="Logo of the bar")

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_category"
        verbose_name = "Bar Category"
        verbose_name_plural = "Bar Categories"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the bar Category object.
        """

        return self.name

