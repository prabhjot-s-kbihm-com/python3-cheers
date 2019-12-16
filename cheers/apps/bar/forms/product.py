from django import forms

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.models import ModelBarProduct


class FormBarProduct(forms.ModelForm):
    """
    This form handle the product data
    """

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control required'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 8, 'class': 'form-control'}),
                                  required=False)                              

    # owner = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'custom-select'}),
    #                                queryset=ModelAccountUser.objects.filter(is_bar_owner=True))

    class Meta:
        model = ModelBarProduct
        fields = ('name', 'image', 'description')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', '')
        super(FormBarProduct, self).__init__(*args, **kwargs)

        # if self.request:
        #     self.fields['owner'].initial = self.request.user.id

    def save(self, *args, **kwargs):
       kwargs['commit']=False
       obj = super(FormBarProduct, self).save(*args, **kwargs)
       if self.request:
           obj.owner = self.request.user
       obj.save()
       return obj        