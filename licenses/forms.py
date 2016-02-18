from django import forms
from licenses.models import License


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = '__all__'
