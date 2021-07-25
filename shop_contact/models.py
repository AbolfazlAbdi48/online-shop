from django.db import models


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    subject = models.CharField(max_length=150, verbose_name='موضوع')
    text = models.TextField(verbose_name='متن پیام')
    status = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')

    class Meta:
        verbose_name = 'تماس'
        verbose_name_plural = 'تماس ها'

    def __str__(self):
        return self.subject
