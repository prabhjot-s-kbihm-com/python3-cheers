from django import forms

class CountryForm(forms.Form):
    name = forms.CharField(label="Country Name", widget=forms.TextInput(attrs={'class': 'form-control required'}))
    is_enabled = forms.BooleanField(label="Enable", widget=forms.CheckboxInput(attrs={'class': 'form-control required'}))