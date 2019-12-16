from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from cheers.apps.bar.forms.bar import FormBar
from cheers.apps.bar.models import ModelBar


class ViewBarUpdate(LoginRequiredMixin, UpdateView):
    form_class = FormBar
    template_name = "bar/add-bar.html"
    success_url = reverse_lazy("bar:list")
    model = ModelBar

    def get_form_kwargs(self):
        kwargs = super(ViewBarUpdate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return  reverse_lazy("bar:drinks", kwargs={"pk":self.object.id})