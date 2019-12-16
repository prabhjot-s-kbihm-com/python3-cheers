from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from cheers.apps.bar.forms.product import FormBarProduct
from cheers.apps.bar.models import ModelBarProduct


class ViewBarDrinkUpdate(SuccessMessageMixin,UpdateView):
    """
    This class handle the add drinks.
    """
    form_class = FormBarProduct
    model = ModelBarProduct
    template_name = "bar/add-drink.html"
    success_message = "Drink Updated Successfully"

    def get_success_url(self):
        return reverse_lazy("bar:drink-detail", kwargs={'pk':self.object.id})
