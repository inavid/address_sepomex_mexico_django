#Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404

#Rest framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Serializers
from address_service.modules.sepomex.serializers import SepomexSerializer

# Models
from address_service.modules.sepomex.models import Sepomex

class SepomexViewSet(viewsets.ReadOnlyModelViewSet):
   """ Sepomex View Set """
   queryset = Sepomex.objects.all()
   serializer_class = SepomexSerializer