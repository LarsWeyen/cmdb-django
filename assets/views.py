from django.shortcuts import render,redirect
from django.db.models import Count
from django.http import HttpResponse
from .models import Type, Asset

def dashboard(request):
    type_names = Type.objects.all()
    counts = {type_name.name: Asset.objects.filter(type=type_name).count() for type_name in type_names}
    

    context = {
        'types': type_names,
        'counts': counts,
    }
    return render(request,'assets/dashboard.html',context)

