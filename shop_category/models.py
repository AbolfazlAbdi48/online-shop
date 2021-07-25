from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی ها')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
