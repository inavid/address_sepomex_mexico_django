""" address_service URL Configuration """

# Django
from django.contrib import admin
from django.urls import include, path

# Rest framework
from rest_framework import routers

urlpatterns = [
    path('api/v1/', include('address_service.modules.address.urls')),
    path('api/v1/', include('address_service.modules.sepomex.urls')),
    path('admin/', admin.site.urls),
]