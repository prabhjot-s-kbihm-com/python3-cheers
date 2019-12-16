from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from cheers.apps.bar.forms.bar import FormBar
from cheers.apps.bar.models import ModelBar, ModelBarProduct


class ViewBarPublish(LoginRequiredMixin, UpdateView):
    """
    This class handle the bar drinks
    """

    template_name = "bar/publish.html"
    model = ModelBar
    fields = ['publish']

    def get_success_url(self):
        return reverse_lazy("bar:detail", kwargs={"pk":self.object.id})