from django import forms
from .models import Asset, Camera

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        exclude = ['type']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'
        exclude=['asset']
        widgets={
            field: forms.TextInput(attrs={'class':'form-field'})
            for field in model._meta.fields
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'