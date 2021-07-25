from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q


# Create your models here.

class ArticleManager(models.Manager):
    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = RichTextUploadingField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='', verbose_name='عکس')
    active = models.BooleanField(verbose_name='فعال / غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ArticleManager()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return f'/blog/article/{self.id}'
