import os
from random import randint

from django.db import models


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    number_random_1 = randint(2000, 200000)
    number_random_2 = randint(2000, 200000)
    final_name = f"{number_random_1}-vogafods-logo-{number_random_2}{ext}"
    return f"setting/{final_name}"


class Setting(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    keywords = models.CharField(max_length=300, verbose_name='کلمات کلیدی')
    favicon = models.ImageField(upload_to='', verbose_name='آیکون سایت')
    email = models.CharField(max_length=200, verbose_name='ایمیل سایت')
    phone = models.CharField(max_length=200, verbose_name='شماره تلفن')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.title
