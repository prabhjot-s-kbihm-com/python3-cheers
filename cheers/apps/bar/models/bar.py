from django.contrib.gis.geos import Point
from django.contrib.postgres.fields import JSONField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db.models import PointField
from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.models import ModelBarCategory, ModelBarProduct
from cheers.apps.base.models import ModelBaseCountry


class ModelBar(models.Model):
    """
    Store the data of bar.
    """

    owner = models.ForeignKey(ModelAccountUser, related_name="bars",
                              on_delete=models.CASCADE, help_text="Owner of the bar.")

    country = models.ForeignKey(ModelBaseCountry, related_name="bars",
                                on_delete=models.SET_NULL, null=True, help_text="Country of the bar.")

    name = models.CharField(max_length=500, help_text="Name of the bar.")

    address = models.TextField()
    latitude = models.DecimalField(max_digits=30, decimal_places=15, help_text="Latitude of bar address")

    longitude = models.DecimalField(max_digits=30, decimal_places=15, help_text="Longitude of bar address")

    drinks = models.ManyToManyField(ModelBarProduct, blank=True, related_name="bars")

    location = PointField(null=True, blank=True, srid=4326)
    description = models.TextField(blank=True, null=True)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(null=True, blank=True)
    bar_category = models.ManyToManyField(ModelBarCategory, related_name="bars")
    bar_timings = JSONField(default=dict)
    publish = models.BooleanField(default=False, help_text="Show the bar on app according to publish status")
    logo = models.ImageField(upload_to="bar/",
                             null=True, blank=True,
                             help_text="Logo of the bar")

    bar_photography = models.ImageField(upload_to="bar/photography/",
                             null=True, blank=True,
                             help_text="Logo of the bar")

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar"
        verbose_name = "Bar"
        verbose_name_plural = "Bars"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the bar object.
        """

        return self.name

    def save(self, *args, **kwargs):
        # keep location point in sync with lat, long
        if self.latitude and self.longitude:
            self.location = Point(float(self.longitude), float(self.latitude))

        return super(ModelBar, self).save(*args, **kwargs)

    @property
    def logo_preview(self):
        return self.logo.url if self.logo else '/static/images/dummy-logo2.jpg'

    @property
    def bar_photography_preview(self):
        return self.bar_photography.url if self.bar_photography else '/static/images/bar.jpeg'
