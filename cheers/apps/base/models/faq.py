from django.db import models
from django.utils.translation import ugettext_lazy as _


class ModelBaseFAQ(models.Model):
    """
    This model store the FAQ of website
    """

    question = models.CharField(max_length=500, help_text="Question about the product")
    answer = models.TextField()

    class Meta:
        db_table = "base_faq"
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ's")

    def __str__(self):
        return self.question