from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from cheers.apps.bar.models import ModelBar


class ViewBarDetail(LoginRequiredMixin, DetailView):
    """
    This class handle the detail of the bar.
    """
    #TODO add permission for user based restriction
    model = ModelBar
    template_name = "bar/detail.html"