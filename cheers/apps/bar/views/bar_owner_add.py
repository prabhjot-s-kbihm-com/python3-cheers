from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cheers.apps.account.forms.user_admin import FormAccountUserAdmin


class ViewBarOwnerAdd(SuccessMessageMixin, CreateView):
    """
    This class is used for bar owners
    """

    form_class = FormAccountUserAdmin
    template_name = "bar/add-bar-owner.html"
    success_url = reverse_lazy("bar:owners")
    success_message = "New Bar Owner added successfully"
