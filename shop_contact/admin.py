from django.contrib import admin

# Register your models here.
from .models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'status']
    list_filter = ['status']
    list_editable = ['status']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactAdmin)
