from django.shortcuts import render

from shop_order.models import Order
from shop_product.models import Product
from shop_setting.models import Setting
from shop_slider.models import Slider


def header(request):
    site_setting = Setting.objects.first()
    active_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    len_order_detail = 0
    if active_order is not None:
        len_order_detail = len(active_order.orderdetail_set.all())

    context = {
        'setting': site_setting,
        'order_detail': len_order_detail
    }
    return render(request, 'shared/Header.html', context)


def footer(request):
    context = {}
    return render(request, 'shared/Footer.html', context)


def slider(request):
    active_slider = Slider.objects.filter(active=True).all()

    context = {
        'slider': active_slider
    }
    return render(request, 'shared/slider_component.html', context)


def meta_tags(request):
    site_setting = Setting.objects.first()

    context = {
        'setting': site_setting
    }
    return render(request, 'shared/mata_tags_component.html', context)


def home_page(request):
    last_products = Product.objects.get_active_product().order_by('-id').all()[:5]

    context = {
        'title': 'صفحه اصلی | فروشگاه ووگا فودز',
        'slider_title': 'محصولات ارگانیک و طبیعی',
        'slider_text': 'ارسال سریع توسط فروشگاه',
        'last_products': last_products,
    }
    return render(request, 'home_page.html', context)
