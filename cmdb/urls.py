from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("assets.urls")),
    path('details/',include('details.urls'))
]
