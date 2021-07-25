from django.contrib import admin

# Register your models here.
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'city']
    list_filter = ['city', 'name']

    class Meta:
        model = Address


admin.site.register(Address, AddressAdmin)
