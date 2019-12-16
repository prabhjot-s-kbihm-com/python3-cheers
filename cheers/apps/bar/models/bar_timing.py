from django.db import models

from cheers.apps.bar.models import ModelBar


class ModelBarTiming(models.Model):
    """
    Store the timings of bar.
    """

    DAY_CHOICES = (('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),
                   ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday'))


    bar = models.ForeignKey(ModelBar, on_delete=models.CASCADE, related_name="timings")
    day = models.CharField(choices=DAY_CHOICES, max_length=100, help_text="Day when open the bar.")
    start_time = models.CharField(max_length=100, help_text="Timing of opening the bar.",
                                  null=True, blank=True)

    end_time = models.CharField(max_length=100, help_text="Timing of closing the bar.",
                                null=True, blank=True)

    is_closed = models.BooleanField(default=False)

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "bar_timing"
        verbose_name = "Bar Timing"
        verbose_name_plural = "Bar Timings"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the bar timing object.
        """

        return self.bar.name