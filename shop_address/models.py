from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Address(models.Model):
    name = models.CharField(max_length=120, verbose_name='نام')
    family = models.CharField(max_length=120, verbose_name='نام خانوادگی')
    city = models.CharField(max_length=120, verbose_name='شهر')
    full_address = models.TextField(verbose_name='آدرس')
    post_code = models.IntegerField(verbose_name='کدپستی')
    phone_number = models.CharField(max_length=100, verbose_name='شماره تلفن')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    def __str__(self):
        return self.city
