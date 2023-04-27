from django.shortcuts import render
from assets.models import Asset, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply, RFID, DVR, QRScanner,IPC,Distrispot

def cameraTable(request):
    cameras = Camera.objects.all()
    breadcrumbs = [{
        'name': 'Cameras',
        'route': "overview:cameras"
    },
    ]
    context = {'cameras':cameras,'breadcrumbs':breadcrumbs}

    return render(request,'overview/camera-table.html',context)

def dvrTable(request):
    dvrs= DVR.objects.all()
    breadcrumbs = [{
        'name': 'DVRs',
        'route': "overview:dvrs"
    },
    ]
    context = {'dvrs':dvrs,'breadcrumbs':breadcrumbs}

    return render(request,'overview/dvr-table.html',context)

def lcdTable(request):
    lcds= LCD.objects.all()
    breadcrumbs = [{
        'name': 'LCDs',
        'route': "overview:lcds"
    },
    ]
    context = {'lcds':lcds,'breadcrumbs':breadcrumbs}

    return render(request,'overview/lcd-table.html',context)

def rfidTable(request):
    rfids= RFID.objects.all()
    breadcrumbs = [{
        'name': 'Routers',
        'route': "overview:routers"
    },
    ]
    context = {'rfids':rfids,'breadcrumbs':breadcrumbs}

    return render(request,'overview/rfid-table.html',context)

def switchTable(request):
    switchs= Switch.objects.all()
    breadcrumbs = [{
        'name': 'Switches',
        'route': "overview:switches"
    },
    ]
    context = {'switchs':switchs,'breadcrumbs':breadcrumbs}

    return render(request,'overview/switch-table.html',context)

def customerTable(request):
    customers= Customer.objects.all()
    breadcrumbs = [{
        'name': 'Customers',
        'route': "overview:customers"
    },
    ]
    context = {'customers':customers,'breadcrumbs':breadcrumbs}

    return render(request,'overview/customer-table.html',context)

def qrScannerTable(request):
    qrScanners= QRScanner.objects.all()
    breadcrumbs = [{
        'name': 'QR Scanners',
        'route': "overview:qrscanners"
    },
    ]
    context = {'qrScanners':qrScanners,'breadcrumbs':breadcrumbs}

    return render(request,'overview/qrscanner-table.html',context)

def ipcTable(request):
    ipcs= IPC.objects.all()
    breadcrumbs = [{
        'name': 'IPCs',
        'route': "overview:ipcs"
    },
    ]
    context = {'ipcs':ipcs,'breadcrumbs':breadcrumbs}

    return render(request,'overview/ipc-table.html',context)

def routerTable(request):
    routers= Router.objects.all()
    breadcrumbs = [{
        'name': 'Routers',
        'route': "overview:routers"
    },
    ]
    context = {'routers':routers,'breadcrumbs':breadcrumbs}

    return render(request,'overview/router-table.html',context)

def powerSupplyTable(request):
    psus= PowerSupply.objects.all()
    breadcrumbs = [{
        'name': 'Power Supplies',
        'route': "overview:psus"
    },
    ]
    context = {'psus':psus,'breadcrumbs':breadcrumbs}

    return render(request,'overview/psu-table.html',context)

def lcbTable(request):
    lcbs= LCB.objects.all()
    breadcrumbs = [{
        'name': 'LCBs',
        'route': "overview:lcbs"
    },
    ]
    context = {'lcbs':lcbs,'breadcrumbs':breadcrumbs}

    return render(request,'overview/lcb-table.html',context)

def assetsTable(request):
    assets= Asset.objects.all()
    breadcrumbs = [{
        'name': 'Assets',
        'route': "overview:assets"
    },
    ]
    context = {'assets':assets,'breadcrumbs':breadcrumbs}

    return render(request,'overview/assets-table.html',context)

# def locationsTable(request):
#     locations= Location.objects.all()
#     context = {'locations':locations}

#     return render(request,'overview/locations-table.html',context)

def distrispotsTable(request):
    distrispots= Distrispot.objects.all()
    breadcrumbs = [{
        'name': 'Distrispots',
        'route': "overview:distrispots"
    },
    ]
    context = {'distrispots':distrispots,'breadcrumbs':breadcrumbs}

    return render(request,'overview/distrispot-table.html',context)