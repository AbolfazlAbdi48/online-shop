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
    final_name = f"{number_random_1}-vogafods-slider-{number_random_2}{ext}"
    return f"slider/{final_name}"


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    text = models.CharField(max_length=250, verbose_name='متن')
    link = models.CharField(max_length=200, verbose_name='لینک دکمه')
    active = models.BooleanField(verbose_name='فعال / غیر فعال')
    background_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='پس زمینه')

    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self.title
