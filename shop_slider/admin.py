from django.contrib import admin

# Register your models here.
from .models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    list_filter = ['active']
    list_editable = ['active']

    class Meta:
        model = Slider


admin.site.register(Slider, SliderAdmin)
