from django.contrib.auth.models import User
from django.db import models
from shop_address.models import Address
from shop_product.models import Product

# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='رداخت شده / نشده')
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE, verbose_name='آدرس ارسال')
    is_send = models.BooleanField(default=False, verbose_name='ارسال شده / نشده')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید'

    def __str__(self):
        return f'{self.owner.username}-{self.id}'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبدخرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت خرید')
    count = models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات سبد خرید'

    def __str__(self):
        return self.product.title

    def get_detail_price(self):
        return self.price * self.count
