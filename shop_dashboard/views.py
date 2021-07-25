from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from shop_account.models import UserProfile
from shop_order.models import Order

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    active_user = User.objects.filter(id=request.user.id).first()
    user_profile: UserProfile = UserProfile.objects.filter(user_id=request.user.id).first()

    context = {
        'title': 'داشبورد | فروشگاه ووگا فودز',
        'slider_title': 'دسترسی راحت',
        'slider_text': 'دسترسی راحت به بخش های مختلف سایت ، دسترسی به آخرین سفارشات و ...',
        'user': active_user,
        'profile': user_profile
    }
    return render(request, 'dashboard/dashboard.html', context)


@user_passes_test(lambda u: u.is_superuser)
def dashboard_orders(request):
    orders = Order.objects.filter(is_paid=True).order_by('-id').all()

    context = {
        'title': 'داشبورد | فروشگاه ووگا فودز',
        'slider_title': 'دسترسی راحت',
        'slider_text': 'دسترسی راحت به بخش های مختلف سایت ، دسترسی به آخرین سفارشات و ...',
        'about_orders':'کاربران',
        'orders': orders
    }
    return render(request, 'dashboard/dashboard_orders.html', context)


@user_passes_test(lambda u: u.is_superuser)
def dashboard_orders_send(request):
    orders = Order.objects.filter(is_paid=True, is_send=True).order_by('-id').all()

    context = {
        'title': 'داشبورد | فروشگاه ووگا فودز',
        'slider_title': 'دسترسی راحت',
        'slider_text': 'دسترسی راحت به بخش های مختلف سایت ، دسترسی به آخرین سفارشات و ...',
        'about_orders': 'ارسال شده',
        'orders': orders
    }
    return render(request, 'dashboard/dashboard_orders.html', context)


@user_passes_test(lambda u: u.is_superuser)
def dashboard_orders_un_send(request):
    orders = Order.objects.filter(is_paid=True, is_send=False, ).order_by('-id').all()

    context = {
        'title': 'داشبورد | فروشگاه ووگا فودز',
        'slider_title': 'دسترسی راحت',
        'slider_text': 'دسترسی راحت به بخش های مختلف سایت ، دسترسی به آخرین سفارشات و ...',
        'about_orders': 'ارسال نشده',
        'orders': orders
    }
    return render(request, 'dashboard/dashboard_orders.html', context)


@user_passes_test(lambda u: u.is_superuser)
def dashboard_order_derail(request, *args, **kwargs):
    order_id = kwargs.get('orderId')
    active_order: Order = Order.objects.filter(id=order_id).first()
    if active_order is None:
        raise Http404

    order_detail = active_order.orderdetail_set.all()

    context = {
        'title': 'داشبورد | فروشگاه ووگا فودز',
        'slider_title': 'دسترسی راحت',
        'slider_text': 'دسترسی راحت به بخش های مختلف سایت ، دسترسی به آخرین سفارشات و ...',
        'order': active_order,
        'order_detail': order_detail
    }
    return render(request, 'dashboard/dashboard_order.html', context)
