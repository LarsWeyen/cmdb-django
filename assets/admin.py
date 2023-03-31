from django.contrib import admin
from .models import Asset, Customer, LCD, Location, Resources, Type, Camera, DVR, LCB, QRScanner, RFID, NetworkDevice, Switch, Router

admin.site.register(Type)
admin.site.register(Asset)
admin.site.register(Location)
admin.site.register(Customer)
admin.site.register(LCD)
