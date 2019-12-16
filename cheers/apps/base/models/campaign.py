from django.db import models
from django.utils.translation import ugettext_lazy as _

from cheers.apps.base.models.base import ModelAbstractBase


class ModelBaseCampaign(ModelAbstractBase):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        ordering = ['name']
        db_table = "base_coupon_campaign"
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")

    def __str__(self):
        return self.name
