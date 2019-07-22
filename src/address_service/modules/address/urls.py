""" Address API router configuration """
# Django
from django.urls import include, path

# Rest framework
from rest_framework import routers

# Custom
from address_service.modules.address import views

router = routers.DefaultRouter()
router.register(r'address', views.AddressViewSet)

urlpatterns = [
    path('', include(router.urls))
]