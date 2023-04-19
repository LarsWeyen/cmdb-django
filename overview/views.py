from django.shortcuts import render
from assets.models import Asset, Location, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply, RFID, DVR, QRScanner,IPC

def cameraTable(request):
    cameras = Camera.objects.all()
    context = {'cameras':cameras}

    return render(request,'overview/camera-table.html',context)

def dvrTable(request):
    dvrs= DVR.objects.all()
    context = {'dvrs':dvrs}

    return render(request,'overview/dvr-table.html',context)

def lcdTable(request):
    lcds= LCD.objects.all()
    context = {'lcds':lcds}

    return render(request,'overview/lcd-table.html',context)

def rfidTable(request):
    rfids= RFID.objects.all()
    context = {'rfids':rfids}

    return render(request,'overview/rfid-table.html',context)

def switchTable(request):
    switchs= Switch.objects.all()
    context = {'switchs':switchs}

    return render(request,'overview/switch-table.html',context)

def customerTable(request):
    customers= Customer.objects.all()
    context = {'customers':customers}

    return render(request,'overview/customer-table.html',context)

def qrScannerTable(request):
    qrScanners= QRScanner.objects.all()
    context = {'qrScanners':qrScanners}

    return render(request,'overview/qrscanner-table.html',context)

def ipcTable(request):
    ipcs= IPC.objects.all()
    context = {'ipcs':ipcs}

    return render(request,'overview/ipc-table.html',context)

def routerTable(request):
    routers= Router.objects.all()
    context = {'routers':routers}

    return render(request,'overview/router-table.html',context)

def powerSupplyTable(request):
    psus= PowerSupply.objects.all()
    context = {'psus':psus}

    return render(request,'overview/psu-table.html',context)

def lcbTable(request):
    lcbs= LCB.objects.all()
    context = {'lcbs':lcbs}

    return render(request,'overview/lcb-table.html',context)

def assetsTable(request):
    assets= Asset.objects.all()
    context = {'assets':assets}

    return render(request,'overview/assets-table.html',context)

def locationsTable(request):
    locations= Location.objects.all()
    context = {'locations':locations}

    return render(request,'overview/locations-table.html',context)