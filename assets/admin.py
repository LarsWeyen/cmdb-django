from django.contrib import admin
from .models import Asset, Customer, LCD, Type, Camera, DVR, LCB, QRScanner, RFID, Switch, Router, Distrispot, IPC, PowerSupply

admin.site.register(Type)
admin.site.register(Asset)
# admin.site.register(Location)
admin.site.register(Customer)
admin.site.register(LCD)
admin.site.register(Camera)
admin.site.register(DVR)
admin.site.register(LCB)
admin.site.register(QRScanner)
admin.site.register(RFID)
admin.site.register(Switch)
admin.site.register(Router)
admin.site.register(Distrispot)
admin.site.register(IPC)
admin.site.register(PowerSupply)
