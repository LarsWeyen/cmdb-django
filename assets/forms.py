from django import forms
from django.forms import TextInput,CheckboxInput
from .models import Asset, Camera, DVR, IPC, LCB, LCD, PowerSupply, QRScanner, RFID, Router, Switch, Customer, Distrispot

from django_select2 import forms as s2forms

class ParentWidget(s2forms.ModelSelect2Widget):
    search_fields = "asset__icontains"
    

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        exclude = ['type']

        widgets = {
            'asset': ParentWidget
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'
        exclude=['asset']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['motion_detection'].widget.attrs.update({'class': 'form-check-input'})

class DvrForm(forms.ModelForm):
    class Meta:
        model = DVR
        fields = '__all__'
        exclude=['asset']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class IpcForm(forms.ModelForm):
    class Meta:
        model = IPC
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class LcbForm(forms.ModelForm):
    class Meta:
        model = LCB
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class LcdForm(forms.ModelForm):
    class Meta:
        model = LCD
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# class LocationForm(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields = '__all__'
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-field'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class PsuForm(forms.ModelForm):
    class Meta:
        model = PowerSupply
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class QRScannerForm(forms.ModelForm):
    class Meta:
        model = QRScanner
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class RfidForm(forms.ModelForm):
    class Meta:
        model = RFID
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class RouterForm(forms.ModelForm):
    class Meta:
        model = Router
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['ip_static'].widget.attrs.update({'class': 'form-check-input'})

class SwitchForm(forms.ModelForm):
    class Meta:
        model = Switch
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class DistrispotForm(forms.ModelForm):
    class Meta:
        model = Distrispot
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

