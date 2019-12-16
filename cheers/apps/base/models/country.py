from django.db import models



class ModelBaseCountry(models.Model):
    """
    This model store the data of country.
    """

    name = models.CharField(max_length=200, help_text="Name of the country", unique=True)
    is_enabled = models.BooleanField(default=True)

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "base_country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the country object.
        """

        return self.name

