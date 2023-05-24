from django.urls import path
from . import views

urlpatterns = [
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('camera/<str:pk>/',views.camera,name='camera'),
    path('dvr/<str:pk>/',views.dvr,name='dvr'),
    path('ipc/<str:pk>/',views.ipc,name='ipc'),
    path('lcb/<str:pk>/',views.lcb,name='lcb'),
    path('lcd/<str:pk>/',views.lcd,name='lcd'),
    path('psu/<str:pk>/',views.psu,name='psu'),
    path('qrscanner/<str:pk>/',views.qrscanner,name='qrscanner'),
    path('rfid/<str:pk>/',views.rfid,name='rfid'),
    path('router/<str:pk>/',views.router,name='router'),
    path('switch/<str:pk>/',views.switch,name='switch'),
    path('distrispot/<str:pk>/',views.distrispot,name='distrispot'),
    path('maintenance/<str:pk>/',views.maintenance,name='maintenance'),
]
