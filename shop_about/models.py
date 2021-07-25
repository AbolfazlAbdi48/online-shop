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
    final_name = f"{number_random_1}-vogafods-about-image-{number_random_2}{ext}"
    return f"about-img/{final_name}"


def upload_video_path(instance, filename):
    name, ext = get_filename_ext(filename)
    number_random_1 = randint(2000, 200000)
    number_random_2 = randint(2000, 200000)
    final_name = f"{number_random_1}-vogafods-about-video-{number_random_2}{ext}"
    return f"about-video/{final_name}"


class AboutUs(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, verbose_name='عکس')
    video = models.FileField(upload_to=upload_video_path, verbose_name='ویدئو')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return self.title
