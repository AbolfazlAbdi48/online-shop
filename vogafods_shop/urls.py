"""vogafods_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from vogafods_shop import settings
from vogafods_shop.views import home_page

urlpatterns = [
    path('', home_page),
    path('home', home_page),
    path('', include('shop_account.urls')),
    path('', include('shop_product.urls')),
    path('', include('shop_about.urls')),
    path('', include('shop_contact.urls')),
    path('', include('shop_order.urls')),
    path('', include('shop_blog.urls')),
    path('', include('shop_dashboard.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
