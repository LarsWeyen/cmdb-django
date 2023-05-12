from django.shortcuts import render
from django.core.cache import cache
from assets.models import Asset, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply, RFID, DVR, QRScanner,IPC,Distrispot, Maintenance, Document

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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
     # Check if there is a cached asset list
    if cache.get('asset-table'):
        # If there is, use the cached asset list
        asset_list = cache.get('asset-table')
    else:
        asset_list=[]
        for asset in assets:
             # Append a dictionary containing the asset's information and details of the component to the asset list
            asset_list.append({
                "id":asset.id,
                "sid":asset.sid,
                "name":asset.name,
                "customer":asset.customer,
                "type":asset.type,
                "parent":asset.parent,
                "created":asset.created,
                "child_id": getattr(asset, f"{asset.type.slug}").first().id,
                "route": f"details:{asset.type.slug}",
                })
        # Cache the asset list for future use
        cache.set('asset-table',asset_list)
    # Breadcrumbs for the template
    breadcrumbs = [{
        'name': 'Assets',
        'route': "overview:assets"
    },
    ]
    context = {'assets':assets,'breadcrumbs':breadcrumbs,"asset_list":asset_list}

    return render(request,'overview/assets-table.html',context)

def distrispotsTable(request):
    distrispots= Distrispot.objects.all()
    breadcrumbs = [{
        'name': 'Distrispots',
        'route': "overview:distrispots"
    },
    ]
    context = {'distrispots':distrispots,'breadcrumbs':breadcrumbs}

    return render(request,'overview/distrispot-table.html',context)

def maintenancesTable(request):
    maintenances = Maintenance.objects.all()
    breadcrumbs = [{
        'name': 'Maintenances',
        'route': "overview:maintenanaces"
    }]
    context = {
        'maintenances':maintenances,
        'breadcrumbs':breadcrumbs
    }
    return render(request,'overview/maintenance-table.html',context)

def maintenanceSpotTable(request,pk):
    maintenances = Maintenance.objects.filter(distrispot_id=pk)
    distrispot_name = Distrispot.objects.get(id=pk).asset.name

    breadcrumbs = [{
        'name': 'Maintenances',
        'route': "overview:maintenances"
    },
    {
        'name': distrispot_name,
        'route':'maintenance'
    }]

    context = {
        'maintenances':maintenances,
        'breadcrumbs':breadcrumbs
               }
    return render(request,'overview/maintenance-table.html',context)

def documentsTable(request):
    document = Document.objects.all()

    context={'documents':document}
    return render(request,'overview/document-table.html',context)

def download(request, id):
    document = get_object_or_404(Document, pk=id)
    response = HttpResponse(document.document, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.document.name}"'
    return response