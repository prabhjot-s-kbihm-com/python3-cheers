from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from cheers.apps.bar.models import  ModelBarProduct


class ViewBarDrinkDetail(LoginRequiredMixin, DetailView):
    """
    This class handle the detail of the drink.
    """
    #TODO add permission for user based restriction
    model = ModelBarProduct
    template_name = "bar/drink-detail.html"

