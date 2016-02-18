from django import forms
from models import Game, Version, ScreenShot


class GameForm(forms.ModelForm):
    class Meta:
        model = Game


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version


class ScreenShotForm(forms.ModelForm):
    class Meta:
        model = ScreenShot
