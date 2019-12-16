from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from cheers.apps.bar.forms.bar import FormBar
from cheers.apps.bar.models import ModelBar, ModelBarProduct


class ViewBarDrinks(LoginRequiredMixin, UpdateView):
    """
    This class handle the bar drinks
    """

    template_name = "bar/bar-drinks.html"
    model = ModelBar
    fields = ['drinks']
    success_url = reverse_lazy("bar:list")


    def get_default_drinks(self):

        drinks = ModelBarProduct.objects.filter(is_default=True).defer('name', 'image', 'owner')
        return drinks

    def get_user_drinks(self):
        # Drinks can added by superuser and bar owner so the avoid duplicate drinks show is default=false drinks.
        drinks = ModelBarProduct.objects.filter(owner=self.request.user, is_default=False).defer('name', 'image', 'owner')
        return drinks

    def get_success_url(self):

        return reverse_lazy("bar:publish", kwargs={"pk":self.object.id})

    # $(".multiple-drinks ul").append('<li><img src = "/media/bar/product/tequila-sunrise.png" alt = "image" ><div class ="custom-control custom-checkbox mt-5" > <input type = "checkbox" class ="custom-control-input" id="Tequila Sunrise-32" name="example1" ><label class ="custom-control-label" for ="Tequila Sunrise-32"> Tequila Sunrise </label></div></li>');