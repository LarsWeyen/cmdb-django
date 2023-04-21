from django import forms
from django.forms import TextInput
from .models import Asset, Camera, DVR, IPC, LCB, LCD, PowerSupply, QRScanner, RFID, Router, Switch, Customer, Distrispot

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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class DvrForm(forms.ModelForm):
    class Meta:
        model = DVR
        fields = '__all__'
        exclude=['asset']
        widgets= {
            'storage_capacity': TextInput(attrs={'placeholder':'Storage in Gigabytes'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class IpcForm(forms.ModelForm):
    class Meta:
        model = IPC
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class LcbForm(forms.ModelForm):
    class Meta:
        model = LCB
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class LcdForm(forms.ModelForm):
    class Meta:
        model = LCD
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

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
            field.widget.attrs['class'] = 'form-field'

class PsuForm(forms.ModelForm):
    class Meta:
        model = PowerSupply
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class QRScannerForm(forms.ModelForm):
    class Meta:
        model = QRScanner
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class RfidForm(forms.ModelForm):
    class Meta:
        model = RFID
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class RouterForm(forms.ModelForm):
    class Meta:
        model = Router
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class SwitchForm(forms.ModelForm):
    class Meta:
        model = Switch
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'

class DistrispotForm(forms.ModelForm):
    class Meta:
        model = Distrispot
        fields = '__all__'
        exclude=['asset']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-field'