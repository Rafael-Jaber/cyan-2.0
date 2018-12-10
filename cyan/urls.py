
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('administrador/', include('apps.adm.dash.urls')),
    path('admin/', admin.site.urls),
]
