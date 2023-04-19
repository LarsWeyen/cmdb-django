from django.shortcuts import render

from assets.models import Asset, Location, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply, RFID, DVR, QRScanner,IPC

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    context={
        'customer':customer
    }

    return render(request, 'details/customer-details.html',context)


def camera(request,pk):
    camera = Camera.objects.get(id=pk)
    asset = Asset.objects.get(id=camera.asset.id)
    context={
        'camera':camera,
        'asset':asset
    }

    return render(request, 'details/camera-details.html',context)

def location(request,pk):
    location = Location.objects.get(id=pk)
    context={
        'location':location
    }

    return render(request, 'details/location-details.html',context)



def dvr(request,pk):
    dvr = DVR.objects.get(id=pk)
    asset = Asset.objects.get(id=dvr.asset.id)
    context={
        'dvr':dvr,
        'asset':asset
    }

    return render(request, 'details/dvr-details.html',context)

def ipc(request,pk):
    ipc = IPC.objects.get(id=pk)
    asset = Asset.objects.get(id=ipc.asset.id)
    context={
        'ipc':ipc,
        'asset':asset
    }

    return render(request, 'details/ipc-details.html',context)

def lcb(request,pk):
    lcb = LCB.objects.get(id=pk)
    asset = Asset.objects.get(id=lcb.asset.id)
    context={
        'lcb':lcb,
        'asset':asset
    }

    return render(request, 'details/lcb-details.html',context)

def lcd(request,pk):
    lcd = LCD.objects.get(id=pk)
    asset = Asset.objects.get(id=lcd.asset.id)
    context={
        'lcd':lcd,
        'asset':asset
    }

    return render(request, 'details/lcd-details.html',context)

def psu(request,pk):
    psu = PowerSupply.objects.get(id=pk)
    asset = Asset.objects.get(id=psu.asset.id)
    context={
        'psu':psu,
        'asset':asset
    }

    return render(request, 'details/psu-details.html',context)

def qrscanner(request,pk):
    qrscanner = QRScanner.objects.get(id=pk)
    asset = Asset.objects.get(id=qrscanner.asset.id)
    context={
        'qrscanner':qrscanner,
        'asset':asset
    }

    return render(request, 'details/qrscanner-details.html',context)

def rfid(request,pk):
    rfid = RFID.objects.get(id=pk)
    asset = Asset.objects.get(id=rfid.asset.id)
    context={
        'rfid':rfid,
        'asset':asset
    }

    return render(request, 'details/rfid-details.html',context)

def router(request,pk):
    router = Router.objects.get(id=pk)
    asset = Asset.objects.get(id=router.asset.id)
    context={
        'router':router,
        'asset':asset
    }

    return render(request, 'details/router-details.html',context)

def switch(request,pk):
    switch = Switch.objects.get(id=pk)
    asset = Asset.objects.get(id=switch.asset.id)
    context={
        'switch':switch,
        'asset':asset
    }

    return render(request, 'details/switch-details.html',context)