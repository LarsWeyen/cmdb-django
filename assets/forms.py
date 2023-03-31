from django import forms
from .models import Camera

class CameraForm(forms.ModelForm):
    password = forms.CharField()
    class Meta:
        model = Camera
        fields = '__all__'