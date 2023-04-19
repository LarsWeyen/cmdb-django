from django.contrib import admin
from django.urls import path, include

app_name = 'details'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("assets.urls")),
    path('details/',include(('details.urls',"details"),namespace="details")),
    path('overview/',include(('overview.urls','overview'),namespace='overview'))
]
