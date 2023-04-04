from django.shortcuts import render,redirect
from django.db.models import Count
from django.http import HttpResponse
from .forms import AssetForm
from .models import Type, Asset, Location, Customer, LCD, LCB, Camera, Switch, Router, PowerSupply

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

    context = {'form':form,
               'types': type_names,
               'locations':locations,
               'customers': customers,
               'parents':parent_assets
               }
    return render(request,'assets/create-asset.html',context)