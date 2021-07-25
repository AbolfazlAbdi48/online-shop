from django.contrib import admin

# Register your models here.
from .models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_paid', 'is_send']
    list_filter = ['is_paid', 'is_send']
    list_editable = ['is_send']

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
