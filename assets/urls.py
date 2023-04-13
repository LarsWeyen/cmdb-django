from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('create-asset',views.createAsset,name='create-asset'),
    path('camera',views.cameraTable,name='camera'),
    path('dvr',views.dvrTable,name='dvr'),
    path('lcd',views.lcdTable,name='lcd'),
    path('rfid',views.rfidTable,name='rfid'),
    path('switch',views.switchTable,name='switch'),
    path('customer',views.customerTable,name='customer'),
    path('qrscanner',views.qrScannerTable,name='qrscanner'),
    path('ipc',views.ipcTable,name='ipc'),
    path('router',views.routerTable,name='router'),
    path('psu',views.powerSupplyTable,name='psu'),
    path('lcb',views.lcbTable,name='lcb'),
    path('assets',views.assetsTable,name='assets'),
    path('locations',views.locationsTable,name='locations'),
    path('update-camera/<str:pk>/',views.updateCamera,name='update-camera'),
]


