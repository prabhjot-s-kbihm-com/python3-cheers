from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ViewPromotions(TemplateView):
    template_name = "promotions/coming_soon.html"