from django.contrib import admin

# Register your models here.
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['__str__', 'parent']
    list_editable = ['parent']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
