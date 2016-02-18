from django import forms
from models import Company, Developer


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
