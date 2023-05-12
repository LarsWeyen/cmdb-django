from django.urls import path, include
from . import views

app_name='assets'

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('create-asset/',views.createAsset,name='create-asset'),
    path('create-customer/',views.createCustomer,name='create-customer'),
    path('update/<str:type>/<str:pk>/',views.update,name='update'),
    path('update-customer/<str:pk>/',views.updateCustomer,name='update-customer'),
    path('delete/<str:type>/<str:pk>/',views.delete,name="delete"),
    path('distrispots/sync',views.sync_distrispots,name="sync-distrispots"),
    path('create-maintenance/',views.createMaintenance,name='create-maintenance'),
    path('update-maintenance/<str:pk>/',views.updateMaintenance,name='update-maintenance'),
    path('upload-document/',views.uploadDocument,name='upload-document'),
]


