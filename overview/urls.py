from django.urls import path, include
from . import views

app_name='overview'

urlpatterns = [
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
    path('distrispots/',views.distrispotsTable,name='distrispots'),
    path('maintenances/',views.maintenancesTable,name='maintenances'),
    path('maintenance/<str:pk>',views.maintenanceSpotTable,name="spot-maintenance"),
    path('documents/',views.documentsTable,name="documents"),
    path('download/<int:id>/', views.download, name='download'),
]
