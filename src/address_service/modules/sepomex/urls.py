""" Sepomex API router configuration """
# Django
from django.urls import include, path

# Rest framework
from rest_framework import routers

# Custom
from address_service.modules.sepomex import views

router = routers.DefaultRouter()
router.register(r'sepomex', views.SepomexViewSet)

urlpatterns = [
    path('', include(router.urls))
]