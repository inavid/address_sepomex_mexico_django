#Django
from django.contrib import admin

#Models
from address_service.modules.address.models import Address

class AddressAdmin(admin.ModelAdmin):
    pass

admin.site.register(Address, AddressAdmin)