from django.contrib import admin

# Register your models here.
from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_filter = ['title']

    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)
