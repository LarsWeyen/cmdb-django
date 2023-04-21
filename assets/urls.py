from django.urls import path, include
from . import views

app_name='assets'

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('create-asset/',views.createAsset,name='create-asset'),
    path('create-customer/',views.createCustomer,name='create-customer'),
    # path('create-location/',views.createLocation,name='create-location'),
    # path('update-location/<str:pk>/',views.updateLocation,name='update-location'),
    path('update/<str:type>/<str:pk>/',views.update,name='update'),
    path('update-customer/<str:pk>/',views.updateCustomer,name='update-customer'),
    path('delete/<str:type>/<str:pk>/',views.delete,name="delete"),
]


