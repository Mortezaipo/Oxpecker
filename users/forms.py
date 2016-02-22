from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            return first_name
        raise forms.ValidationError("This field is required.")
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name:
            return last_name
        raise forms.ValidationError("This field is required.")
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            return email
        raise forms.ValidationError("This field is required.")
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return make_password(password)
        raise forms.ValidationError("This field is required.")