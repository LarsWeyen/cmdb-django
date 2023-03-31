from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Type

def dashboard(request):
    types = Type.objects.all()
    context={'types':types}
    return render(request,'assets/dashboard.html',context)

