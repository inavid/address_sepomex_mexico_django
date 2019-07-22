""" Model of sepomex table """
#Python
import uuid

#Django
from django.db import models


class Sepomex(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    d_codigo = models.CharField(max_length=100, null=True, blank=True)
    d_asenta = models.CharField(max_length=100, null=True, blank=True)
    d_tipo_asenta = models.CharField(max_length=100, null=True, blank=True)
    D_mnpio = models.CharField(max_length=100, null=True, blank=True)
    d_estado = models.CharField(max_length=100, null=True, blank=True)
    d_ciudad = models.CharField(max_length=100, null=True, blank=True)
    d_CP = models.CharField(max_length=100, null=True, blank=True)
    c_estado = models.CharField(max_length=100, null=True, blank=True)
    c_oficina = models.CharField(max_length=100, null=True, blank=True)
    c_CP = models.CharField(max_length=100, null=True, blank=True)
    c_tipo_asenta = models.CharField(max_length=100, null=True, blank=True)
    c_mnpio = models.CharField(max_length=100, null=True, blank=True)
    id_asenta_cpcons = models.CharField(max_length=100, null=True, blank=True)
    d_zona = models.CharField(max_length=100, null=True, blank=True)
    c_cve_ciudad = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)