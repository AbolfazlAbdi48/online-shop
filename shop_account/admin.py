from django.contrib import admin

# Register your models here.
from shop_account.models import UserProfile


admin.site.register(UserProfile)
