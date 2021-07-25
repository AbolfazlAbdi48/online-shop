from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active', 'product_count']
    list_filter = ['title', 'active']
    list_editable = ['active']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
