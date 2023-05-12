from django.contrib import admin
from .models import Asset, Customer, LCD, Type, Camera, DVR, LCB, QRScanner, RFID, Switch, Router, Distrispot, IPC, PowerSupply, Maintenance,Document

admin.site.register(Type)
admin.site.register(Asset)
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
admin.site.register(Maintenance)
admin.site.register(PowerSupply)
admin.site.register(Document)
