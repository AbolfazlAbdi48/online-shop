# Generated by Django 3.2.2 on 2021-05-09 20:35

from django.db import migrations, models
import shop_slider.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to=shop_slider.models.upload_image_path, verbose_name='پس زمینه'),
        ),
    ]
