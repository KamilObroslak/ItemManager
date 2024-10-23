from django.contrib import admin
from .models import ClientProfile, MerchantProfile

class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name' ,'phone_number')
    search_fields = ('first_name', 'phone_number')

class MerchantProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone_number')
    search_fields = ('first_name', 'phone_number')

admin.site.register(ClientProfile, ClientProfileAdmin)
admin.site.register(MerchantProfile, MerchantProfileAdmin)
