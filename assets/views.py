from django.shortcuts import render,redirect
from django.db.models import Count
from django.http import HttpResponse
from .forms import AssetForm
from .models import Type, Asset, Location, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply, RFID, DVR, QRScanner,IPC

def dashboard(request):
    type_names = Type.objects.all()
    counts = {type_name.slug: Asset.objects.filter(type=type_name).count() for type_name in type_names}
    

    context = {
        'types': type_names,
        'counts': counts,
    }
    return render(request,'assets/dashboard.html',context)

def createAsset(request):
    form = AssetForm()
    type_names = Type.objects.all()
    locations = Location.objects.all()
    customers = Customer.objects.all()
    parent_assets = Asset.objects.all()

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
            print(request.POST.get('manufacturer'))
            LCD.objects.create(
                name = request.POST.get('lcd_name'),
                asset=asset,
                manufacturer = request.POST.get('manufacturer'),
                model = request.POST.get('model'),
                serial = request.POST.get('serial'),
                resolution = request.POST.get('resolution'),
                refresh_rate = request.POST.get('refresh_rate'),
            )

        if asset_type.slug == 'power_supply':
            PowerSupply.objects.create(
                name = request.POST.get('psu_name'),
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
                name = request.POST.get('camera_name'),
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
                name = request.POST.get('switch_name'),
                asset=asset,
                manufacturer = request.POST.get('switch_manufacturer'),
                model = request.POST.get('switch_model'),
                serial = request.POST.get('switch_serial'),
                num_ports = request.POST.get('switch_num_ports'),
                mac_address = request.POST.get('switch_mac_address'),
            )

        if asset_type.slug == 'router':
            Router.objects.create(
                name = request.POST.get('router_name'),
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
                name = request.POST.get('rfid_name'),
                asset=asset,
                manufacturer = request.POST.get('rfid_manufacturer'),
                model = request.POST.get('rfid_model'),
                serial = request.POST.get('rfid_serial'),
                voltage = request.POST.get('rfid_voltage'),
                frequency = request.POST.get('rfid_frequency'),
            )
        
        if asset_type.slug == 'dvr':
            DVR.objects.create(
                name = request.POST.get('dvr_name'),
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
                name = request.POST.get('qr_scanner_name'),
                asset=asset,
                manufacturer = request.POST.get('qr_scanner_manufacturer'),
                model = request.POST.get('qr_scanner_model'),
                serial = request.POST.get('qr_scanner_serial'),
                resolution = request.POST.get('qr_scanner_resolution'),
                port_type = request.POST.get('qr_scanner_port_type'),
            )

        if asset_type.slug == 'ipc':
            IPC.objects.create(
                name = request.POST.get('ipc_name'),
                asset=asset,
                manufacturer = request.POST.get('ipc_manufacturer'),
                model = request.POST.get('ipc_model'),
                serial = request.POST.get('ipc_serial'),
                cpu = request.POST.get('ipc_cpu'),
                android_version = request.POST.get('ipc_android_version'),
            )

        if asset_type.slug == 'lcb':
            LCB.objects.create(
                name = request.POST.get('lcb_name'),
                asset=asset,
                manufacturer = request.POST.get('lcb_manufacturer'),
                model = request.POST.get('lcb_model'),
                serial = request.POST.get('lcb_serial'),
                connector = request.POST.get('lcb_connector'),
                voltage = request.POST.get('lcb_voltage'),
            )
        
        redirect('dashboard')
        
    context = {'form':form,
               'types': type_names,
               'locations':locations,
               'customers': customers,
               'parents':parent_assets
               }
    return render(request,'assets/create-asset.html',context)