# Generated by Django 3.2.2 on 2021-05-12 01:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
    ]
