""" Address Viewsets """
#Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404

#Rest framework
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework import status

# Serializers
from address_service.modules.address.serializers import AddressSerializer

# Models
from address_service.modules.address.models import Address

class AddressViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """ Address View Set """
    queryset = Address.objects.filter(is_active=True)
    serializer_class = AddressSerializer

    # def delete(self, request, *args, **kwargs):
    #     print(request)
    #     print(self)
    #     return self.destroy(request, *args, **kwargs)