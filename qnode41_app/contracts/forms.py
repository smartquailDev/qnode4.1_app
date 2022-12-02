from django import forms
from .models import Contract


class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['first_name', 'last_name', 'email', 'address',
                  'CI', 'city']
