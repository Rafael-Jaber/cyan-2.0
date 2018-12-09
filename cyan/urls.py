
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.adm.dash.urls')),
    path('admin/', admin.site.urls),
]
