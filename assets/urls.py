from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('create-asset',views.createAsset,name='create-asset')
]


