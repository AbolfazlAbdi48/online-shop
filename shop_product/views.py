from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from shop_order.forms import UserNewOrderForm
from .models import Product


class ProductList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.get_active_product()

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['title'] = 'محصولات | فروشگاه ووگا فودز'
        context['slider_title'] = 'محصولات فروشگاه'
        context['slider_text'] = 'محصولات ارگانیک و طبیعی'
        return context


def product_detail(request, *args, **kwargs):
    product_id = kwargs.get('productId')
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': product_id})
    product = Product.objects.get_product_by_id(product_id)
    if product is None:
        raise Http404

    product_count = True
    if product.product_count <= 0:
        product_count = False

    related_product = Product.objects.filter(categories__product=product, active=True).distinct()

    context = {
        'title': f'{product.title} | فروشگاه ووگا فودز',
        'product': product,
        'product_count': product_count,
        'related_product': related_product,
        'slider_title': f'{product.title}',
        'order_form': new_order_form
    }
    return render(request, 'products/product_detail.html', context)


class SearchList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 12

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active_product()

