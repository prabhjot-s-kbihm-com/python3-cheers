from django.shortcuts import get_object_or_404, render
from django.template import loader
from cheers.apps.base.models.country import ModelBaseCountry
from cheers.apps.country.forms import CountryForm

def index(request):
    countries = ModelBaseCountry.objects.all()
    context = {
        'countries': countries
    }
    return render(request, 'countries/index.html', context)

def edit(request, country_id):
    country = get_object_or_404(ModelBaseCountry, pk=country_id)
    form = CountryForm()
    return render(request, 'countries/edit.html', {'country': country, 'form': form})    
