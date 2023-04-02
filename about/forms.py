from django import forms
from .models import CarCollection


class CarForm(forms.ModelForm):
    class Meta:
        model = CarCollection
        fields = ("name", "image", "link")
