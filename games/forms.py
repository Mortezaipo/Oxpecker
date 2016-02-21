from django import forms
from models import Game, Version, ScreenShot


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
        
    def clean_logo(self):
        logo = self.cleaned_data.get('logo', False)
        if logo:
            if logo.content_type == 'image/png':
                return logo
        raise forms.ValidationError('%s file format is not supported. Just PNG file is acceptable.' % logo.content_type)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.content_type == 'image/png':
                return image
        raise forms.ValidationError('%s file format is not supported. Just PNG file is acceptable.' % image.content_type)


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
        

class ScreenShotForm(forms.ModelForm):
    class Meta:
        model = ScreenShot
        fields = "__all__"