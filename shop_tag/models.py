from django.db import models

# Create your models here.
from shop_product.models import Product


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    name = models.CharField(max_length=120, null=True, blank=True, verbose_name='عنوان در url')
    products = models.ManyToManyField(Product, verbose_name='محصولات')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title
