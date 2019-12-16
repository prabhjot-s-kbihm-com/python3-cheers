from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from cheers.apps.bar.models import ModelBar


class ViewBarList(LoginRequiredMixin, ListView):
    """
    This class handle the add bar.
    """

    template_name = "bar/list.html"
    model = ModelBar

    def get_queryset(self):

        queryset = self.model.objects.all()
        bar_owner = self.request.GET.get('owner_id')

        if bar_owner and self.request.user.is_superuser:
            try:
                return queryset.filter(owner__id=bar_owner)
            except ValueError:
                pass

        return queryset.filter(owner=self.request.user)