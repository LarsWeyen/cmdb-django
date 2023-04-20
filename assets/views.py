from django.shortcuts import render,redirect
from django.db.models import Count
from django.http import HttpResponse
from .forms import AssetForm, CameraForm, DvrForm, IpcForm, LcbForm, LcdForm, LocationForm, PsuForm, QRScannerForm, RfidForm, RouterForm, SwitchForm, CustomerForm
from .models import Type, Asset, Location, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply, RFID, DVR, QRScanner,IPC, Distrispot,DistrispotType
from numerize import numerize

def dashboard(request):
    type_names = Type.objects.all()
    counts = {type_name.slug: numerize.numerize(Asset.objects.filter(type=type_name).count()) for type_name in type_names}
    customer_count = numerize.numerize(Customer.objects.all().count()) 
    location_count = numerize.numerize(Location.objects.all().count()) 
    context = {
        'types': type_names,
        'counts': counts,
        'customer_count':customer_count,
        'location_count':location_count
    }
    return render(request,'assets/dashboard.html',context)

def createAsset(request):
    form = AssetForm()
    type_names = Type.objects.all()
    locations = Location.objects.all()
    customers = Customer.objects.all()
    parent_assets = Asset.objects.all()
    distrispot_types = DistrispotType.objects.all()

    if request.method == 'POST':
        asset_type = Type.objects.get(name=request.POST.get('type'))
        asset = Asset.objects.create(
            type=asset_type,
            name=request.POST.get('name'),
            location = Location.objects.get(id=request.POST.get('location')),
            customer = Customer.objects.get(id=request.POST.get('customer')),
            parent = None if request.POST.get('parent') == 'null' else Asset.objects.get(id=request.POST.get('parent'))
        )
        if asset_type.slug == "lcd":        
            LCD.objects.create(
                asset=asset,
                manufacturer = request.POST.get('manufacturer'),
                model = request.POST.get('model'),
                serial = request.POST.get('serial'),
                resolution = request.POST.get('resolution'),
                refresh_rate = request.POST.get('refresh_rate'),
            )

        if asset_type.slug == 'power_supply':
            PowerSupply.objects.create(
                asset=asset,
                manufacturer = request.POST.get('psu_manufacturer'),
                model = request.POST.get('psu_model'),
                serial = request.POST.get('psu_serial'),
                voltage = request.POST.get('psu_voltage'),
                wattage = request.POST.get('psu_wattage'),
                form_factor = request.POST.get('psu_form_factor'),
            )
        
        if asset_type.slug == 'camera':
            Camera.objects.create(
                asset=asset,
                manufacturer = request.POST.get('camera_manufacturer'),
                model = request.POST.get('camera_model'),
                serial = request.POST.get('camera_serial'),
                ip_address = request.POST.get('camera_ip_address'),
                firmware = request.POST.get('camera_firmware'),
                frame_rate = request.POST.get('camera_frame_rate'),
                resolution = request.POST.get('camera_resolution'),
                compression_format = request.POST.get('camera_format'),
                motion_detection = request.POST.get('camera_motion'),
                username = request.POST.get('camera_username'),
                password = request.POST.get('camera_password'),
            )
        
        if asset_type.slug == 'switch':
            Switch.objects.create(
                asset=asset,
                manufacturer = request.POST.get('switch_manufacturer'),
                model = request.POST.get('switch_model'),
                serial = request.POST.get('switch_serial'),
                num_ports = request.POST.get('switch_num_ports'),
                mac_address = request.POST.get('switch_mac_address'),
            )

        if asset_type.slug == 'router':
            Router.objects.create(
                asset=asset,
                manufacturer = request.POST.get('router_manufacturer'),
                model = request.POST.get('router_model'),
                serial = request.POST.get('router_serial'),
                hostname = request.POST.get('router_hostname'),
                ip_address = request.POST.get('router_ip_address'),
                firmware = request.POST.get('router_firmware'),
                username = request.POST.get('router_username'),
                password = request.POST.get('router_password'),
                ip_static = request.POST.get('router_ip_static')
            )
        
        if asset_type.slug == 'rfid':
            RFID.objects.create(
                asset=asset,
                manufacturer = request.POST.get('rfid_manufacturer'),
                model = request.POST.get('rfid_model'),
                serial = request.POST.get('rfid_serial'),
                voltage = request.POST.get('rfid_voltage'),
                frequency = request.POST.get('rfid_frequency'),
            )
        
        if asset_type.slug == 'dvr':
            DVR.objects.create(
                asset=asset,
                manufacturer = request.POST.get('dvr_manufacturer'),
                model = request.POST.get('dvr_model'),
                serial = request.POST.get('dvr_serial'),
                ip_address = request.POST.get('dvr_ip_address'),
                firmware = request.POST.get('dvr_firmware'),
                username = request.POST.get('dvr_username'),
                password = request.POST.get('dvr_password'),
                storage_capacity = request.POST.get('dvr_storage'),
            )

        if asset_type.slug == 'qr_scanner':
            QRScanner.objects.create(
                asset=asset,
                manufacturer = request.POST.get('qr_scanner_manufacturer'),
                model = request.POST.get('qr_scanner_model'),
                serial = request.POST.get('qr_scanner_serial'),
                resolution = request.POST.get('qr_scanner_resolution'),
                port_type = request.POST.get('qr_scanner_port_type'),
            )

        if asset_type.slug == 'ipc':
            IPC.objects.create(
                asset=asset,
                manufacturer = request.POST.get('ipc_manufacturer'),
                model = request.POST.get('ipc_model'),
                serial = request.POST.get('ipc_serial'),
                cpu = request.POST.get('ipc_cpu'),
                android_version = request.POST.get('ipc_android_version'),
            )

        if asset_type.slug == 'lcb':
            LCB.objects.create(
                asset=asset,
                manufacturer = request.POST.get('lcb_manufacturer'),
                model = request.POST.get('lcb_model'),
                serial = request.POST.get('lcb_serial'),
                connector = request.POST.get('lcb_connector'),
                voltage = request.POST.get('lcb_voltage'),
            )
        
        if asset_type.slug == 'distrispot':
            Distrispot.objects.create(
                asset=asset,
                slots_num = request.POST.get('distrispot_slots_num'),
                type = DistrispotType.objects.get(id=request.POST.get('distrispot_type')),
            )
        
        redirect('assets:dashboard')

    context = {'form':form,
               'types': type_names,
               'locations':locations,
               'customers': customers,
               'parents':parent_assets,
               'distrispot_types':distrispot_types
               }
    return render(request,'assets/create-asset.html',context)

def createCustomer(request):
    form = CustomerForm()

    if request.method =='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('assets:dashboard')
    
    context = {'form':form}
    return render(request,'assets/create-customer.html',context)

def createLocation(request):
    form = LocationForm()

    if request.method =='POST':
        form = LocationForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('assets:dashboard')
    
    context = {'form':form}
    return render(request,'assets/create-location.html',context)

def updateLocation(request,pk):
    location = Location.objects.get(id=pk)
    form = LocationForm(instance=location)
    if request.method =='POST':
        form = LocationForm(request.POST,instance=location)   
        if form.is_valid():           
             form.save()
             return redirect('overview:locations')
    context={
        'form':form,       
        'location':location
    }
    return render(request,'assets/update-location.html',context)

def updateCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method =='POST':
        form = CustomerForm(request.POST,instance=customer)   
        if form.is_valid():           
             form.save()
             return redirect('overview:customers')
    context={
        'form':form,       
        'customer':customer
    }
    return render(request,'assets/update-customer.html',context)

def update(request,pk,type):
    if type == 'camera':
        camera = Camera.objects.get(id=pk)
        asset = Asset.objects.get(id=camera.asset.id)
        assetForm = AssetForm(instance=asset)
        form = CameraForm(instance=camera)
        item = camera
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = CameraForm(request.POST,instance=camera)   
            if form.is_valid() and assetForm.is_valid():    
                 form.save()
                 assetForm.save()
                 return redirect('overview:cameras')
            
    if type == 'dvr':
        dvr = DVR.objects.get(id=pk)
        asset = Asset.objects.get(id=dvr.asset.id)
        assetForm = AssetForm(instance=asset)
        form = DvrForm(instance=dvr)
        item = dvr
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = DvrForm(request.POST,instance=dvr)
            if form.is_valid() and assetForm.is_valid():
             
                form.save()
                assetForm.save()
                return redirect('overview:dvrs')
    
    if type == 'ipc':
        ipc = IPC.objects.get(id=pk)
        asset = Asset.objects.get(id=ipc.asset.id)
        assetForm = AssetForm(instance=asset)
        form = IpcForm(instance=ipc)
        item = ipc
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = IpcForm(request.POST,instance=ipc)   
            if form.is_valid() and assetForm.is_valid():
                
                form.save()
                assetForm.save()
                return redirect('overview:ipcs')
    
    if type == 'lcb':
        lcb = LCB.objects.get(id=pk)
        asset = Asset.objects.get(id=lcb.asset.id)
        assetForm = AssetForm(instance=asset)
        form = LcbForm(instance=lcb)
        item = lcb
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = LcbForm(request.POST,instance=lcb)   
            if form.is_valid() and assetForm.is_valid():
                
                form.save()
                assetForm.save()
                return redirect('overview:lcbs')

    if type == 'lcd':
        lcd = LCD.objects.get(id=pk)
        asset = Asset.objects.get(id=lcd.asset.id)
        assetForm = AssetForm(instance=asset)
        form = LcdForm(instance=lcd)
        item = lcd
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = LcdForm(request.POST,instance=lcd)   
            if form.is_valid() and assetForm.is_valid():
                
                form.save()
                assetForm.save()
                return redirect('overview:lcds')
            
    if type == 'psu':
        psu = PowerSupply.objects.get(id=pk)
        asset = Asset.objects.get(id=psu.asset.id)
        assetForm = AssetForm(instance=asset)
        form = PsuForm(instance=psu)
        item = psu
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = PsuForm(request.POST,instance=psu)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                return redirect('overview:psus')

    if type == 'qrscanner':
        qrscanner = QRScanner.objects.get(id=pk)
        asset = Asset.objects.get(id=qrscanner.asset.id)
        assetForm = AssetForm(instance=asset)
        form = QRScannerForm(instance=qrscanner)
        item = qrscanner
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = QRScannerForm(request.POST,instance=qrscanner)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                return redirect('overview:qrscanners')

    if type == 'rfid':
        rfid = RFID.objects.get(id=pk)
        asset = Asset.objects.get(id=rfid.asset.id)
        assetForm = AssetForm(instance=asset)
        form = RfidForm(instance=rfid)
        item = rfid
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = RfidForm(request.POST,instance=rfid)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                return redirect('overview:rfids')
            
    if type == 'router':
        router = Router.objects.get(id=pk)
        asset = Asset.objects.get(id=router.asset.id)
        assetForm = AssetForm(instance=asset)
        form = RouterForm(instance=router)
        item = router
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = RouterForm(request.POST,instance=router)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                return redirect('overview:routers')

    if type == 'switch':
        switch = Switch.objects.get(id=pk)
        asset = Asset.objects.get(id=switch.asset.id)
        assetForm = AssetForm(instance=asset)
        form = SwitchForm(instance=switch)
        item = switch
        if request.method =='POST':
            assetForm = AssetForm(request.POST,instance=asset)
            form = SwitchForm(request.POST,instance=switch)   
            if form.is_valid() and assetForm.is_valid():    
                form.save()
                assetForm.save()
                return redirect('overview:switches')

    context={
        'form':form,
        'assetForm':assetForm,
        'item': item
    }
    return render(request,'assets/update.html',context)

def delete(request,type,pk):
    if type == 'asset':
        item = Asset.objects.get(id=pk)
        if request.method == 'POST':
            Asset.objects.filter(id=pk).delete()
            redirect('assets:dashboard')
        
    
    elif type == 'location':
        item = Location.objects.get(id=pk)
        if request.method == 'POST':
            Location.objects.filter(id=pk).delete()
            redirect('overview:locations')
    
    elif type == 'customer':
        item = Customer.objects.get(id=pk)
        if request.method == 'POST':
            Customer.objects.filter(id=pk).delete()
            redirect('overview:customers')
   
    context={
        'item':item
    }
    return render(request,'assets/delete.html',context)