# Generated by Django 3.2.2 on 2021-05-12 01:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0002_alter_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات'),
        ),
    ]