from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('create-asset/',views.createAsset,name='create-asset'),
    path('cameras/',views.cameraTable,name='cameras'),
    path('dvrs/',views.dvrTable,name='dvrs'),
    path('lcds/',views.lcdTable,name='lcds'),
    path('rfids/',views.rfidTable,name='rfids'),
    path('switches/',views.switchTable,name='switches'),
    path('customers/',views.customerTable,name='customers'),
    path('qrscanners/',views.qrScannerTable,name='qrscanners'),
    path('ipcs/',views.ipcTable,name='ipcs'),
    path('routers/',views.routerTable,name='routers'),
    path('psus/',views.powerSupplyTable,name='psus'),
    path('lcbs/',views.lcbTable,name='lcbs'),
    path('assets/',views.assetsTable,name='assets'),
    path('locations/',views.locationsTable,name='locations'),
    path('update-location/<str:pk>/',views.updateLocation,name='update-location'),
    path('update/<str:type>/<str:pk>/',views.update,name='update'),
    path('camera/<str:pk>/',views.camera,name='camera'),
    path('location/<str:pk>/',views.location,name='location'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('update-customer/<str:pk>/',views.updateCustomer,name='update-customer'),
    path('dvr/<str:pk>/',views.dvr,name='dvr'),
    path('ipc/<str:pk>/',views.ipc,name='ipc'),
    path('lcb/<str:pk>/',views.lcb,name='lcb'),
    path('lcd/<str:pk>/',views.lcd,name='lcd'),
    path('psu/<str:pk>/',views.psu,name='psu'),
    path('qrscanner/<str:pk>/',views.qrscanner,name='qrscanner'),
    path('rfid/<str:pk>/',views.rfid,name='rfid'),
    path('router/<str:pk>/',views.router,name='router'),
    path('switch/<str:pk>/',views.switch,name='switch'),
]


