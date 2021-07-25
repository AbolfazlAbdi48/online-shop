import os
from random import randint

from django.contrib.auth.models import User
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
    final_name = f"{number_random_1}-vogafods-profile-{number_random_2}{ext}"
    return f"user-profile/{final_name}"


class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس پروفایل')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'پروفایل کاربر'
        verbose_name_plural = 'پروفایل کاربران'

    def __str__(self):
        return self.user.username
