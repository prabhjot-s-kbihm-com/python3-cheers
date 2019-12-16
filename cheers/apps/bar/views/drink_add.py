from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cheers.apps.bar.forms.product import FormBarProduct
from cheers.apps.bar.models import ModelBarProduct


class ViewBarAddDrink(SuccessMessageMixin, CreateView):
    """
    This class handle the add drinks.
    """
    form_class = FormBarProduct
    model = ModelBarProduct
    template_name = "bar/add-drink.html"
    success_message = "New Drink added successfully"

    def get_form_kwargs(self):
        kwargs = super(ViewBarAddDrink, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):

        if self.request.GET.get('bar'):
            return  reverse_lazy("bar:drinks", kwargs={"pk":self.request.GET.get('bar')})
        else:
            reverse_lazy("bar:add-drink")




