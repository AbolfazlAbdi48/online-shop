import os
from random import randint

from django.db import models
from django.db.models import Q

from extension.utils import jalali_converter
from shop_category.models import Category

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    number_random_1 = randint(2000, 200000)
    number_random_2 = randint(2000, 200000)
    final_name = f"{number_random_1}-vogafods-product-{number_random_2}{ext}"
    return f"products/{final_name}"


class ProductManger(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True).all()

    def get_product_by_id(self, product_id):
        return self.get_queryset().filter(id=product_id).first()

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(categories__title__icontains=query) |
                Q(tag__name__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    sale_count = models.IntegerField(default=0, verbose_name='تعداد فروش')
    product_count = models.IntegerField(verbose_name='تعداد موجودی')
    categories = models.ManyToManyField(Category, null=True, blank=True, verbose_name='دسته بندی ها')
    active = models.BooleanField(verbose_name='فعال / غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت')

    objects = ProductManger()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return f'{self.id}/{self.title.replace(" ", "-")}'

    def created_jalali_date(self):
        return jalali_converter(self.created_at)
