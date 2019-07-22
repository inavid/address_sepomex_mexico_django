#Django
from django.contrib import admin

#Models
from address_service.modules.sepomex.models import Sepomex

class SepomexAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sepomex, SepomexAdmin)