from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.timezone import now

from shop_address.models import Address
from shop_order.forms import UserNewOrderForm
from shop_order.models import Order, OrderDetail
from shop_product.models import Product


@login_required(login_url='/login')
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id)

        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count <= 0:
            count = 1
        product = Product.objects.get_product_by_id(product_id)

        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')

    return redirect('/')


@login_required(login_url='/login')
def order_list(request):
    context = {
        'title': 'سبد خرید | فروشگاه ووگا فودز',
        'slider_title': 'سبد خرید شما',
        'slider_text': 'خریدی امن را تجربه کنید'
    }
    active_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if active_order is not None:
        order_detail = active_order.orderdetail_set.all()
        context['order_detail'] = order_detail
        result = 0
        for order in order_detail:
            result += order.price * order.count
        context['sum'] = result

    context['addresses'] = Address.objects.filter(user_id=request.user.id).all()

    if request.method == "POST":
        address = request.POST['address']

        active_order.is_paid = True
        active_order.payment_date = now()
        active_order.address_id = address
        active_order.save()

        for product in active_order.orderdetail_set.all():
            product.product.product_count -= product.count
            product.product.sale_count += product.count
            product.product.save()
        return redirect('/account/paid-order')

    return render(request, 'order/order_list.html', context)
