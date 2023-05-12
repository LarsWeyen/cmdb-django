from django.shortcuts import render,redirect
from django.db.models import Count
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
import requests
from overview.views import download
import os
from django.core.files.storage import FileSystemStorage,default_storage
from django.urls import reverse
from .forms import AssetForm, CameraForm, DvrForm, IpcForm, LcbForm, LcdForm, PsuForm, QRScannerForm, RfidForm, RouterForm, SwitchForm, CustomerForm, DistrispotForm, MaintenanceForm, DocumentForm
from .models import Type, Asset, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply, RFID, DVR, QRScanner,IPC, Distrispot,Maintenance,Document
from numerize import numerize
from .utilities import OAuth2Adapter
from django.contrib import messages

def dashboard(request):
    type_names = Type.objects.all()
     # Check if dashboard counts are already in cache
    if cache.get('dashboard-counts'):
        counts = cache.get('dashboard-counts')
    else:
        # If not, get counts for each asset type
        counts = {type_name.slug: numerize.numerize(Asset.objects.filter(type=type_name).count()) for type_name in type_names}
        # Set counts in cache
        cache.set('dashboard-counts',counts)
    customer_count = numerize.numerize(Customer.objects.all().count()) 
    
    context = {
        'types': type_names,
        'counts': counts,
        'customer_count':customer_count,
    }

    return render(request,'assets/dashboard.html',context)

def createAsset(request):
    # First instantiates a form for each type of asset, 
    # so that it can be displayed for the appropriate asset type on the frontend.
    cameraForm = CameraForm(prefix="cameraForm")
    lcdForm = LcdForm(prefix="lcdForm")
    psuForm= PsuForm(prefix="psuForm")
    switchForm= SwitchForm(prefix="switchForm")
    routerForm= RouterForm(prefix="routerForm")
    rfidForm= RfidForm(prefix="rfidForm")
    dvrForm= DvrForm(prefix="dvrForm")
    qrscannerForm= QRScannerForm(prefix="qrscannerForm")
    ipcForm= IpcForm(prefix="ipcForm")
    lcbForm= LcbForm(prefix="lcbForm")
    distrispotForm= DistrispotForm(prefix="distrispotForm")
    form = AssetForm()
    type_names = Type.objects.all()
    customers = Customer.objects.all()
    parent_assets = Asset.objects.all()

    breadcrumbs = [{
        'name': 'New Asset',
        'route': "overview:assets"
    }]

    # If the request method is POST, then a new asset has been submitted
    if request.method == 'POST':
        # Get the asset type of the submitted asset
        asset_type = Type.objects.get(name=request.POST.get('type'))
        asset = Asset.objects.create(
            type=asset_type,
            name=request.POST.get('name'),
            customer = Customer.objects.get(id=request.POST.get('customer')),
            parent = None if request.POST.get('parent') == 'null' else Asset.objects.get(id=request.POST.get('parent'))
        )
        # Check what the submitted asset type is
        if asset_type.slug == "lcd":        
            # Populate the form with the submitted data
            lcdForm = LcdForm(request.POST,prefix="lcdForm")
            if lcdForm.is_valid():
                # Add the newly created asset to the LCB object
                lcd = lcdForm.save(commit=False)
                lcd.asset = asset
                lcd.save()
                messages.success(request,'Created LCD Asset!')
                return redirect('assets:dashboard')

        elif asset_type.slug == 'power_supply':
            psuForm = PsuForm(request.POST,prefix="psuForm")
            if psuForm.is_valid():
                psu = psuForm.save(commit=False)
                psu.asset = asset
                psu.save()
                messages.success(request,'Created Power Supply Asset!')
                return redirect('assets:dashboard')
        
        elif asset_type.slug == 'camera':
            cameraForm = CameraForm(request.POST,prefix="cameraForm")
            if cameraForm.is_valid():
                camera = cameraForm.save(commit=False)
                camera.asset = asset
                camera.save()
                messages.success(request,'Created Camera Asset!')
                return redirect('assets:dashboard')
        
        elif asset_type.slug == 'switch':
            switchForm = SwitchForm(request.POST,prefix="switchForm")
            if switchForm.is_valid():
                switch = switchForm.save(commit=False)
                switch.asset = asset
                switch.save()
                messages.success(request,'Created Switch Asset!')
                return redirect('assets:dashboard')

        elif asset_type.slug == 'router':
            routerForm = RouterForm(request.POST,prefix="routerForm")
            if routerForm.is_valid():
                router = routerForm.save(commit=False)
                router.asset = asset
                router.save()
                messages.success(request,'Created Router Asset!')
                return redirect('assets:dashboard')
        
        elif asset_type.slug == 'rfid':
            rfidForm = RfidForm(request.POST,prefix="rfidForm")
            if rfidForm.is_valid():
                rfid = rfidForm.save(commit=False)
                rfid.asset = asset
                rfid.save()
                messages.success(request,'Created RFID Asset!')
                return redirect('assets:dashboard')
        
        elif asset_type.slug == 'dvr':
            dvrForm = DvrForm(request.POST,prefix="dvrForm")
            if dvrForm.is_valid():
                dvr = dvrForm.save(commit=False)
                dvr.asset = asset
                dvr.save()
                messages.success(request,'Created DVR Asset!')
                return redirect('assets:dashboard')

        elif asset_type.slug == 'qr_scanner':
            qrscannerForm = QRScannerForm(request.POST,prefix="qrscannerForm")
            if qrscannerForm.is_valid():
                qrscanner = qrscannerForm.save(commit=False)
                qrscanner.asset = asset
                qrscanner.save()
                messages.success(request,'Created QR Scanner Asset!')
                return redirect('assets:dashboard')

        elif asset_type.slug == 'ipc':
            ipcForm = IpcForm(request.POST,prefix="ipcForm")
            if ipcForm.is_valid():
                ipc = ipcForm.save(commit=False)
                ipc.asset = asset
                ipc.save()
                messages.success(request,'Created IPC Asset!')
                return redirect('assets:dashboard')

        elif asset_type.slug == 'lcb':
            lcbForm = LcbForm(request.POST,prefix="lcbForm")
            if lcbForm.is_valid():
                lcb = lcbForm.save(commit=False)
                lcb.asset = asset
                lcb.save()
                messages.success(request,'Created LCB Asset!')
                return redirect('assets:dashboard')
        
        elif asset_type.slug == 'distrispot':
            distrispotForm = DistrispotForm(request.POST,prefix="distrispotForm")
            if distrispotForm.is_valid():
                distrispot = distrispotForm.save(commit=False)
                distrispot.asset = asset
                distrispot.save()
                messages.success(request,'Created Distrispot Asset!')
                return redirect('assets:dashboard')

    context = {'form':form,
               'types': type_names,
               'customers': customers,
               'parents':parent_assets,
               'routerForm':routerForm,
               'cameraForm':cameraForm,
               'lcdForm':lcdForm,
               'psuForm': psuForm,
               'switchForm':switchForm,
               'rfidForm':rfidForm,
               'dvrForm':dvrForm,
               'qrscannerForm':qrscannerForm,
               'ipcForm':ipcForm,
               'lcbForm': lcbForm,
               'distrispotForm':distrispotForm,
               'breadcrumbs':breadcrumbs
               }
    return render(request,'assets/create-asset.html',context)

def createCustomer(request):
    form = CustomerForm()
    breadcrumbs = [{
        'name': 'New Customer',
        'route': "overview:customers"
    }]

    if request.method =='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
             form.save()
             messages.success(request,'Customer Created!')
             return redirect('assets:dashboard')
    
    context = {'form':form,'breadcrumbs':breadcrumbs}
    return render(request,'assets/create-customer.html',context)

def updateCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    breadcrumbs = [{
        'name': 'Customers',
        'route': "overview:customers"
    },
    {
        'name': customer.name,
        'route': 'details:customer'
    }]

    if request.method =='POST':
        form = CustomerForm(request.POST,instance=customer)   
        if form.is_valid():           
             form.save()
             messages.success(request,'Customer Updated!')
             return redirect('overview:customers')
    context={
        'form':form,       
        'customer':customer,
        'breadcrumbs':breadcrumbs
    }
    return render(request,'assets/update-customer.html',context)

def updateMaintenance(request,pk):
    maintenance = Maintenance.objects.get(id=pk)
    form = MaintenanceForm(instance=maintenance)
    breadcrumbs = [{
        'name': 'Maintenances',
        'route': "overview:maintenances"
    },
    {
        'name': maintenance.sid,
        'route': 'details:maintenance'
    }]

    if request.method =='POST':
        form = MaintenanceForm(request.POST,instance=maintenance)   
        if form.is_valid():           
             form.save()
             messages.success(request,'Maintenance Updated!')
             return redirect('overview:maintenances')
    context={
        'form':form,       
        'maintenance':maintenance,
        'breadcrumbs':breadcrumbs
    }
    return render(request,'assets/update-maintenance.html',context)

def update(request,pk,type):
    if type == 'camera':
        camera = Camera.objects.get(id=pk)
        asset = Asset.objects.get(id=camera.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'Cameras'
        breadcrumb_route = 'overview:cameras'
        asset_name = asset.name
        # Fills the form with the filtered object
        form = CameraForm(instance=camera)
        item = camera
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = CameraForm(request.POST,instance=camera)   
            # If the Camera and asset forms are valid they will be saved
            if form.is_valid() and assetForm.is_valid():    
                 form.save()
                 assetForm.save()
                 messages.success(request,'Camera Updated!')
                 return redirect('overview:cameras')
            
    if type == 'dvr':
        dvr = DVR.objects.get(id=pk)
        asset = Asset.objects.get(id=dvr.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'DVRs'
        breadcrumb_route = 'overview:dvrs'
        asset_name = asset.name
        form = DvrForm(instance=dvr)
        item = dvr
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = DvrForm(request.POST,instance=dvr)
            if form.is_valid() and assetForm.is_valid():
                form.save()
                assetForm.save()
                messages.success(request,'DVR Updated!')
                return redirect('overview:dvrs')
    
    elif type == 'ipc':
        ipc = IPC.objects.get(id=pk)
        asset = Asset.objects.get(id=ipc.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'IPCS'
        breadcrumb_route = 'overview:ipcs'
        asset_name = asset.name
        form = IpcForm(instance=ipc)
        item = ipc
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = IpcForm(request.POST,instance=ipc)   
            if form.is_valid() and assetForm.is_valid():
                form.save()
                assetForm.save()
                messages.success(request,'IPC Updated!')
                return redirect('overview:ipcs')
    
    elif type == 'lcb':
        lcb = LCB.objects.get(id=pk)
        asset = Asset.objects.get(id=lcb.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'LCBs'
        breadcrumb_route = 'overview:lcbs'
        asset_name = asset.name
        form = LcbForm(instance=lcb)
        item = lcb
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = LcbForm(request.POST,instance=lcb)   
            if form.is_valid() and assetForm.is_valid():
                form.save()
                assetForm.save()
                messages.success(request,'LCB Updated!')
                return redirect('overview:lcbs')

    elif type == 'lcd':
        lcd = LCD.objects.get(id=pk)
        asset = Asset.objects.get(id=lcd.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'LCDs'
        breadcrumb_route = 'overview:lcds'
        asset_name = asset.name
        form = LcdForm(instance=lcd)
        item = lcd
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = LcdForm(request.POST,instance=lcd)   
            if form.is_valid() and assetForm.is_valid():
                form.save()
                assetForm.save()
                messages.success(request,'LCD Updated!')
                return redirect('overview:lcds')
            
    elif type == 'psu':
        psu = PowerSupply.objects.get(id=pk)
        asset = Asset.objects.get(id=psu.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'Power Supplies'
        breadcrumb_route = 'overview:psus'
        asset_name = asset.name
        form = PsuForm(instance=psu)
        item = psu
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = PsuForm(request.POST,instance=psu)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                messages.success(request,'Power Supply Updated!')
                return redirect('overview:psus')

    elif type == 'qrscanner':
        qrscanner = QRScanner.objects.get(id=pk)
        asset = Asset.objects.get(id=qrscanner.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'QR Scanners'
        breadcrumb_route = 'overview:qrscanners'
        asset_name = asset.name
        form = QRScannerForm(instance=qrscanner)
        item = qrscanner
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = QRScannerForm(request.POST,instance=qrscanner)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                messages.success(request,'QR Scanner Updated!')
                return redirect('overview:qrscanners')

    elif type == 'rfid':
        rfid = RFID.objects.get(id=pk)
        asset = Asset.objects.get(id=rfid.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'RFIDs'
        breadcrumb_route = 'overview:rfids'
        asset_name = asset.name
        form = RfidForm(instance=rfid)
        item = rfid
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = RfidForm(request.POST,instance=rfid)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                messages.success(request,'RFID Updated!')
                return redirect('overview:rfids')
            
    elif type == 'router':
        router = Router.objects.get(id=pk)
        asset = Asset.objects.get(id=router.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'Routers'
        breadcrumb_route = 'overview:router'
        asset_name = asset.name
        form = RouterForm(instance=router)
        item = router
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = RouterForm(request.POST,instance=router)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                messages.success(request,'Router Updated!')
                return redirect('overview:routers')

    elif type == 'switch':
        switch = Switch.objects.get(id=pk)
        asset = Asset.objects.get(id=switch.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'Switches'
        breadcrumb_route = 'overview:switches'
        asset_name = asset.name
        form = SwitchForm(instance=switch)
        item = switch
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = SwitchForm(request.POST,instance=switch)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                messages.success(request,'Switch Updated!')
                return redirect('overview:switches')
            
    elif type == 'distrispot':
        distrispot = Distrispot.objects.get(id=pk)
        asset = Asset.objects.get(id=distrispot.asset.id)
        assetForm = AssetForm(instance=asset)
        breadcrumb_plural = 'Distrispots'
        breadcrumb_route = 'overview:distrispots'
        asset_name = asset.name
        form = DistrispotForm(instance=distrispot)
        item = distrispot
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = DistrispotForm(request.POST,instance=distrispot)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                messages.success(request,'Distrispot Updated!')
                return redirect('overview:distrispots')
    
    breadcrumbs = [{
        'name': breadcrumb_plural,
        'route': breadcrumb_route
    },
    {
        'name': asset_name,
        'route': '_'
    }]

    context={
        'form':form,
        'assetForm':assetForm,
        'item': item,
        'breadcrumbs':breadcrumbs
    }
    return render(request,'assets/update.html',context)

def delete(request,type,pk):
    # Gets the page from which the delete button has been pressed
    next = request.POST.get('next', '/')
    app = str(request.GET['next']).split('/')[1]
    res = str(request.GET['next']).split('/')[2]
    if type == 'asset':
        item = Asset.objects.get(id=pk)
        if request.method == 'POST':
            Asset.objects.filter(id=pk).delete()
            messages.success(request,'Deleted Asset!')
            # If the button has been pressed on a details page it goes back to the overview of that asset type
            if "details" in app:
                res += 'es' if res == 'switch' else 's'
                return redirect(f'overview:{res}')
            else:
                return redirect(next)
        
    elif type == 'customer':
        item = Customer.objects.get(id=pk)
        if request.method == 'POST':
            Customer.objects.filter(id=pk).delete()
            messages.success(request,'Deleted Customer!')
            return redirect('overview:customers')
    elif type == 'maintenance':
        item = Maintenance.objects.get(id=pk)
        if request.method == 'POST':
            Maintenance.objects.filter(id=pk).delete()
            messages.success(request,'Deleted Maintenance!')
            return redirect('overview:maintenances')
    elif type=='document':
        item = Document.objects.get(id=pk)
        if request.method == 'POST':
            Document.objects.filter(id=pk).delete()
            os.remove('media/'+os.path.basename(item.document.name))
            messages.success(request,'Deleted Document!')
            return redirect(next)

    context={
        'item':item
    }
    return render(request,'assets/delete.html',context)

def sync_distrispots(request):
    oauth_adapter = OAuth2Adapter("Telloport")
    access_token = oauth_adapter.get_token()
    headers = {
        'Authorization': f"Bearer {access_token}",
    }
    response = requests.get(f'{oauth_adapter.url}/api/spots/', headers=headers)
    response.raise_for_status()
    spots = response.json()
    for spot in spots:
       # Extracts the id out of SPT-0001
       id  = ''.join(x for x in spot["id"] if x.isdigit())

       # Checks if the incomming spots are already in the database else it creates them
       asset, asset_created =Asset.objects.get_or_create(
           name = spot['name'],
           type= Type.objects.get(slug='distrispot'),
           customer = Customer.objects.get(id=1)
       )

       distrispot, created = Distrispot.objects.get_or_create(
           id = id,
           slots_num = spot['slots_num'],
           asset=asset,
           type = spot['type'],
           address = spot['address_line_1'],
           city = spot['city'],
           zip_code= spot['zip_code']
        )

    messages.success(request,'Distrispots synchronized!') 

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def createMaintenance(request):
    form = MaintenanceForm()
    breadcrumbs = [{
        'name': 'New Maintenance',
        'route': "overview:maintenances"
    }]
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Maintenance Created!')
            return redirect('assets:dashboard')
        
    context = {
        'form':form,
        'breadcrumbs':breadcrumbs
    }
    return render(request,'assets/create-maintenance.html',context)

def uploadDocument(request):
    form = DocumentForm()
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'File Uploaded!')
            return redirect("overview:documents")
    context = {'form':form}
    return render(request,'assets/upload-document.html',context)

def openDoc(request,pk):
    document = Document.objects.get(id=pk)
    if document.extension() == "pdf":
        with open(document.document.path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
    else:
        return download(request,pk)
    