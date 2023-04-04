from django.shortcuts import render,redirect
from django.db.models import Count
from django.http import HttpResponse
from .forms import AssetForm
from .models import Type, Asset, Location, Customer

def dashboard(request):
    type_names = Type.objects.all()
    counts = {type_name.name: Asset.objects.filter(type=type_name).count() for type_name in type_names}
    

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
        Asset.objects.create(
            type=asset_type,
            name=request.POST.get('name'),
            location = Location.objects.get(id=request.POST.get('location')),
            customer = Customer.objects.get(id=request.POST.get('customer')),
            parent = None if request.POST.get('parent') == 'null' else Asset.objects.get(id=request.POST.get('parent'))
        )

    context = {'form':form,
               'types': type_names,
               'locations':locations,
               'customers': customers,
               'parents':parent_assets
               }
    return render(request,'assets/create-asset.html',context)