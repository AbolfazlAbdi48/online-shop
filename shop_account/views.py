from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from shop_order.models import Order
from .forms import LoginForm, RegisterForm, EditUserForm, CreateAddressForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from shop_address.models import Address
from .models import UserProfile


# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/home')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('/dashboard')
            return redirect('/')

    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/home')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')

        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect(request.GET.get('path'))


@login_required(login_url='/login')
def user_page(request):
    active_user = User.objects.filter(id=request.user.id).first()
    user_profile: UserProfile = UserProfile.objects.filter(user_id=request.user.id).first()
    profile = None
    if user_profile is not None:
        profile = user_profile

    context = {
        'title': 'پنل کاربری | فروشگاه ووگا فودز',
        'slider_title': 'پنل کاربری',
        'slider_text': 'دسترسی به عملیات های انجام شده و ...',
        'user': active_user,
        'profile': profile
    }
    return render(request, 'account/user.html', context)


@login_required(login_url='/login')
def user_edit(request):
    active_user = User.objects.filter(id=request.user.id).first()
    user_profile: UserProfile = UserProfile.objects.filter(user_id=request.user.id).first()

    user_edit_form = EditUserForm(request.POST or None, request.FILES or None,
                                  initial={'last_name': active_user.last_name, 'first_name': active_user.first_name})

    if user_edit_form.is_valid():
        first_name = user_edit_form.cleaned_data.get('first_name')
        last_name = user_edit_form.cleaned_data.get('last_name')
        profile_image = user_edit_form.cleaned_data.get('profile_image')

        active_user.first_name = first_name
        active_user.last_name = last_name
        active_user.save()

        if user_profile is None:
            UserProfile.objects.create(profile_image=profile_image, user_id=request.user.id)
        else:
            user_profile.profile_image = profile_image
            user_profile.save()

        return redirect('/account')

    context = {
        'title': 'ویرایش اطلاعات | فروشگاه ووگا فودز',
        'slider_title': 'پنل کاربری',
        'slider_text': 'ویرایش اطلاعات',
        'user': active_user,
        'edit_form': user_edit_form
    }
    return render(request, 'account/account_edit.html', context)


@login_required(login_url='/login')
def user_address(request):
    address = Address.objects.filter(user_id=request.user.id).all()

    context = {
        'title': 'آدرس | فروشگاه ووگا فودز',
        'slider_title': 'آدرس های شما',
        'slider_text': 'مشاهده و اضافه کردن آدرس',
        'address': address
    }
    return render(request, 'account/account_address.html', context)


@login_required(login_url='/login')
def user_add_address(request):
    active_user = User.objects.filter(id=request.user.id).first()
    address_form = CreateAddressForm(request.POST or None)

    if address_form.is_valid():
        name = address_form.cleaned_data.get('name')
        family = address_form.cleaned_data.get('family')
        city = address_form.cleaned_data.get('city')
        full_address = address_form.cleaned_data.get('full_address')
        post_code = address_form.cleaned_data.get('post_code')
        phone_number = address_form.cleaned_data.get('phone_number')

        Address.objects.create(name=name, family=family, city=city, full_address=full_address, post_code=post_code,
                               phone_number=phone_number, user_id=active_user.id)

        return redirect('/account/address')

    context = {
        'title': 'آدرس | فروشگاه ووگا فودز',
        'slider_title': 'آدرس های شما',
        'slider_text': 'مشاهده و اضافه کردن آدرس',
        'address_form': address_form
    }
    return render(request, 'account/account_add_address.html', context)


@login_required(login_url='/login')
def user_edit_address(request, *args, **kwargs):
    active_user = User.objects.filter(id=request.user.id).first()
    address_id = kwargs['addressId']

    active_address = Address.objects.filter(user_id=active_user.id, id=address_id).first()

    if active_address is None:
        raise Http404
    address_form = CreateAddressForm(request.POST or None,
                                     initial={'name': active_address.name, 'family': active_address.family,
                                              'city': active_address.city, 'post_code': active_address.post_code,
                                              'full_address': active_address.full_address,
                                              'phone_number': active_address.phone_number})

    if address_form.is_valid():
        name = address_form.cleaned_data.get('name')
        family = address_form.cleaned_data.get('family')
        city = address_form.cleaned_data.get('city')
        full_address = address_form.cleaned_data.get('full_address')
        post_code = address_form.cleaned_data.get('post_code')
        phone_number = address_form.cleaned_data.get('phone_number')

        active_address.name = name
        active_address.family = family
        active_address.city = city
        active_address.full_address = full_address
        active_address.post_code = post_code
        active_address.phone_number = phone_number
        active_address.save()

        return redirect('/account/address')

    context = {
        'title': 'آدرس | فروشگاه ووگا فودز',
        'slider_title': 'آدرس های شما',
        'slider_text': 'مشاهده و اضافه کردن آدرس',
        'address_form': address_form
    }
    return render(request, 'account/account_add_address.html', context)


@login_required(login_url='/login')
def user_delete_address(request, *args, **kwargs):
    address_id = kwargs['addressId']
    user_id = request.user.id

    active_address = Address.objects.filter(user_id=user_id, id=address_id).first()
    if active_address is None:
        raise Http404

    active_address.delete()
    return redirect('/account/address')


@login_required(login_url='/login')
def user_paid_orders(request):
    order_detail = Order.objects.filter(owner_id=request.user.id).order_by('-id').all()

    alert = False
    if request.META['HTTP_REFERER'] == f'{request.scheme}://{request.get_host()}/orders':
        alert = True

    context = {
        'title': 'سفارشات | فروشگاه ووگا فودز',
        'slider_title': 'سفارش های شما',
        'slider_text': 'مشاهده',
        'order_detail': order_detail,
        'alert': alert
    }
    return render(request, 'account/user_paid_orders.html', context)


@login_required(login_url='/login')
def user_paid_order_detail(request, *args, **kwargs):
    order_id = kwargs['orderId']
    active_order: Order = Order.objects.filter(owner_id=request.user.id, id=order_id).first()
    order_detail = active_order.orderdetail_set.all()

    context = {
        'title': 'سفارشات | فروشگاه ووگا فودز',
        'slider_title': 'سفارش های شما',
        'slider_text': 'مشاهده',
        'order_detail': order_detail
    }
    return render(request, 'account/user_paid_order_detail.html', context)
