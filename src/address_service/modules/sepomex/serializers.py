""" Sepomex Serializers """
# Django
from django.conf import settings

# Django Rest Framework
from rest_framework import serializers

# Local & Utilities
from address_service.modules.sepomex.models import Sepomex

class SepomexSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sepomex
		fields = (
			'id',
            'd_codigo',
            'd_asenta',
            'D_mnpio',
            'd_estado',
            'd_ciudad',
            'd_CP',
            'id_asenta_cpcons',
            'd_zona',
            'created_at',
            'updated_at'
		)
        