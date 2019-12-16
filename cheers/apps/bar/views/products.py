from django.views.generic import ListView

from cheers.apps.bar.models import ModelBarProduct


class ViewBarProducts(ListView):
    """
    This class handle the list of products
    """

    model = ModelBarProduct
    template_name = "bar/products.html"


    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(owner=self.request.user)