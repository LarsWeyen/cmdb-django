from django.shortcuts import render

from assets.models import Asset, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply, RFID, DVR, QRScanner,IPC, Distrispot, Maintenance

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    breadcrumbs = [{
        'name': 'Customers',
        'route': "overview:customers"
    },
    {
        'name': customer.name,
        'route': 'details:customer'
    }]

    context={
        'customer':customer,
        'breadcrumbs':breadcrumbs
    }

    return render(request, 'details/customer-details.html',context)


def camera(request,pk):
    camera = Camera.objects.get(id=pk)
    asset = Asset.objects.get(id=camera.asset.id)

    breadcrumbs = [{
        'name': 'Cameras',
        'route': "overview:cameras"
    },
    {
        'name': asset.name,
        'route': 'details:camera'
    }]

    context={
        'camera':camera,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/camera-details.html',context)

# def location(request,pk):
#     location = Location.objects.get(id=pk)
#     context={
#         'location':location
#     }

#     return render(request, 'details/location-details.html',context)



def dvr(request,pk):
    dvr = DVR.objects.get(id=pk)
    asset = Asset.objects.get(id=dvr.asset.id)

    breadcrumbs = [{
        'name': 'DVRs',
        'route': "overview:dvrs"
    },
    {
        'name': asset.name,
        'route': 'details:dvr'
    }]

    context={
        'dvr':dvr,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/dvr-details.html',context)

def ipc(request,pk):
    ipc = IPC.objects.get(id=pk)
    asset = Asset.objects.get(id=ipc.asset.id)

    breadcrumbs = [{
        'name': 'IPCs',
        'route': "overview:ipcs"
    },
    {
        'name': asset.name,
        'route': 'details:ipc'
    }]

    context={
        'ipc':ipc,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/ipc-details.html',context)

def lcb(request,pk):
    lcb = LCB.objects.get(id=pk)
    asset = Asset.objects.get(id=lcb.asset.id)

    breadcrumbs = [{
        'name': 'LCBs',
        'route': "overview:lcbs"
    },
    {
        'name': asset.name,
        'route': 'details:lcb'
    }]


    context={
        'lcb':lcb,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/lcb-details.html',context)

def lcd(request,pk):
    lcd = LCD.objects.get(id=pk)
    asset = Asset.objects.get(id=lcd.asset.id)

    breadcrumbs = [{
        'name': "LCDs",
        'route': "overview:lcds"
    },
    {
        'name': asset.name,
        'route': 'details:lcd'
    }]

    context={
        'lcd':lcd,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/lcd-details.html',context)

def psu(request,pk):
    psu = PowerSupply.objects.get(id=pk)
    asset = Asset.objects.get(id=psu.asset.id)
    breadcrumbs = [{
        'name': 'Power Supplies',
        'route': "overview:psus"
    },
    {
        'name': asset.name,
        'route': 'details:psu'
    }]

    context={
        'psu':psu,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/psu-details.html',context)

def qrscanner(request,pk):
    qrscanner = QRScanner.objects.get(id=pk)
    asset = Asset.objects.get(id=qrscanner.asset.id)
    breadcrumbs = [{
        'name': 'QR Scanners',
        'route': "overview:qrscanners"
    },
    {
        'name': asset.name,
        'route': 'details:qrscanners'
    }]

    context={
        'qrscanner':qrscanner,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/qrscanner-details.html',context)

def rfid(request,pk):
    rfid = RFID.objects.get(id=pk)
    asset = Asset.objects.get(id=rfid.asset.id)
    
    breadcrumbs = [{
        'name': 'RFIDS',
        'route': "overview:rfids"
    },
    {
        'name': asset.name,
        'route': 'details:rfid'
    }]

    context={
        'rfid':rfid,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/rfid-details.html',context)

def router(request,pk):
    router = Router.objects.get(id=pk)
    asset = Asset.objects.get(id=router.asset.id)

    breadcrumbs = [{
        'name': 'Routers',
        'route': "overview:routers"
    },
    {
        'name': asset.name,
        'route': 'details:router'
    }]

    context={
        'router':router,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/router-details.html',context)

def switch(request,pk):
    switch = Switch.objects.get(id=pk)
    asset = Asset.objects.get(id=switch.asset.id)

    breadcrumbs = [{
        'name': 'Switches',
        'route': "overview:switches"
    },
    {
        'name': asset.name,
        'route': 'details:switch'
    }]

    context={
        'switch':switch,
        'asset':asset,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/switch-details.html',context)

def distrispot(request,pk):
    distrispot = Distrispot.objects.get(id=pk)
    asset = Asset.objects.get(id=distrispot.asset.id)
    children = Asset.objects.filter(parent=asset.id)
    children_list = []
    for child in children:
        children_list.append({
            "route": f"details:{child.type.slug}",
            "id": getattr(child, f"{child.type.slug}").first().id,
            "name": child.name, 
        })

    breadcrumbs = [{
        'name': 'Distrispots',
        'route': "overview:distrispots"
    },
    {
        'name': asset.name,
        'route': 'details:distrispot'
    }]
    
    context={
        'distrispot':distrispot,
        'asset':asset,
        'children_list': children_list,
        'breadcrumbs':breadcrumbs,
        'documents':getAssetDocuments(asset)
    }

    return render(request, 'details/distrispot-details.html',context)

def maintenance(request,pk):
    maintenance = Maintenance.objects.get(id=pk)

    breadcrumbs = [{
        'name': 'Maintenances',
        'route': "overview:maintenances"
    },
    {
        'name': maintenance.sid,
        'route': 'details:switch'
    }]

    context={
        'maintenance':maintenance,
        'breadcrumbs':breadcrumbs
    }

    return render(request, 'details/maintenance-details.html',context)

def getAssetDocuments(asset):
    return asset.document_set.all()
