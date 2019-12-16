from django.views.generic import ListView

from cheers.apps.account.models import ModelAccountUser


class ViewBarOwners(ListView):
    """
    This class handle list of bar owners.
    """

    model = ModelAccountUser
    template_name = "bar/owners.html"
    queryset = model.objects.filter(is_bar_owner=True)