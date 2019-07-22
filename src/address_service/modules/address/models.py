""" Model of address table """
#Python
import uuid

#Django
from django.db import models

#Project
from address_service.modules.sepomex.models import Sepomex

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sepomex = models.ForeignKey(Sepomex, models.SET_NULL,blank=True,null=True,)
    postal_code = models.CharField(max_length=5)
    street = models.CharField(max_length=100)
    external_number = models.CharField(max_length=100)
    internal_number = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)