from django import forms
from models import Company, Developer


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ["user",]
    
    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        if logo:
            if logo.content_type == 'image/png':
                return logo
            else:
                raise forms.ValidationError('%s file format is not supported. Just PNG file is acceptable.' % logo.content_type)
        raise forms.ValidationError('This field is required.')


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        exclude = ["company",]
        
    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            if picture.content_type == 'image/png':
                return picture
            else:
                raise forms.ValidationError('%s file format is not supported. Just PNG file is acceptable.' % logo.content_type)
        raise forms.ValidationError('This field is required.')
    