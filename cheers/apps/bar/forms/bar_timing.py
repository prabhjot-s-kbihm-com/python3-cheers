from django import forms
from django.forms import inlineformset_factory

from cheers.apps.bar.models import ModelBarTiming, ModelBar


class FormBarTiming(forms.ModelForm):
    """
    This form handle the data of bar timings.
    """

    day = forms.CharField(widget=forms.Select(choices=ModelBarTiming.DAY_CHOICES, attrs={'class': 'custom-select col-md-9'}))



    class Meta:

        model = ModelBarTiming
        fields = ('day', 'start_time', 'end_time', 'is_closed')

BarTimingFormSet = inlineformset_factory(ModelBar, ModelBarTiming, extra=1, exclude=(), form=FormBarTiming)