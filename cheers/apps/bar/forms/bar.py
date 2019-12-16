from django import forms
from django.forms import FileInput

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.models import ModelBar, ModelBarCategory
from cheers.apps.base.models import ModelBaseCountry


class FormBar(forms.ModelForm):
    """
    This form handle the bar data
    """

    name = forms.CharField(label="Name of your bar (displayed in the application)*", widget=forms.TextInput(attrs={'class': 'form-control required'}))

    country = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'custom-select'}),
                                     queryset=ModelBaseCountry.objects.all(), label="City where your bar is located*")

    bar_photography = forms.FileField(widget=FileInput(attrs={'class':"custom-file-input"}))

    address = forms.CharField(widget=forms.TextInput(attrs={'rows': 4, 'class': 'form-control'}),
                              label="Address of your bar (Make sure this is the right location checking on the map below)*")

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 8, 'class': 'form-control', 'maxlength': '1000'}),
                                  required=False, label="Description (Not more than 1000 words)")

    owner = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'custom-select'}),
                                   queryset=ModelAccountUser.objects.filter(is_bar_owner=True))

    class Meta:
        model = ModelBar
        fields = ('owner', 'country', 'name', 'address', 'latitude', 'longitude',
                  'description', 'bar_category', 'logo',  'bar_photography', 'bar_timings')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', '')
        super(FormBar, self).__init__(*args, **kwargs)

        self.fields['bar_category'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['bar_category'].queryset = ModelBarCategory.objects.all()
        self.fields['bar_category'].help_text = ""
        self.fields['bar_category'].label = "Bar Category (can choose multiple choices):"

        if self.request.user.is_bar_owner:
            self.fields['owner'].initial = self.request.user

