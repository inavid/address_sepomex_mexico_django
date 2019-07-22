""" Address Serializers """
# Django Rest Framework
from rest_framework import serializers

# Project
from address_service.modules.address.models import Address
from address_service.modules.sepomex.serializers import SepomexSerializer
from address_service.modules.sepomex.models import Sepomex

class AddressSerializer(serializers.ModelSerializer):
    
    sepomex = SepomexSerializer(read_only=True)
    
    class Meta:
        model = Address
        fields = (
            'id',
            'sepomex',
            'postal_code',
            'street',
            'external_number',
            'internal_number',
            'is_active',
            'created_at',
            'updated_at'
        )
        read_only_fields = ['id','sepomex']
    
    def validate(self, data):
        """
            Check postal code and add internal_num if is empty
        """
        if not "internal_number" in data.keys():
            data['internal_number'] = None
        
        try:
            Sepomex.objects.get(d_codigo=data['postal_code'])
        except Sepomex.DoesNotExist:
            raise serializers.ValidationError('Invalid Postal Code')
        return data

    def create(self, data):
        """
            Create to check if the postal code is founded on sepomex, if not, then we will
            reject the save of this address
        """
        sepomex = Sepomex.objects.get(d_codigo=data['postal_code'])
        address=Address.objects.create(
            sepomex=sepomex,
            postal_code=data['postal_code'],
            street=data['street'],
            external_number=data['external_number'],
            internal_number=data['internal_number']
        )
        return address
