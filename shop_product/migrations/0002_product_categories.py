# Generated by Django 3.2.2 on 2021-05-09 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_category', '0001_initial'),
        ('shop_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_category.category', verbose_name='دسته بندی ها'),
        ),
    ]
