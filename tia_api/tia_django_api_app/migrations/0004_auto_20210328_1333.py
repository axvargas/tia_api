# Generated by Django 3.1.7 on 2021-03-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tia_django_api_app', '0003_profit_by_hour'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='department',
            index=models.Index(fields=['department'], name='departments_departm_5774f9_idx'),
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['order_hour_of_day'], name='orders_order_h_a72ee7_idx'),
        ),
        migrations.AddIndex(
            model_name='order_product',
            index=models.Index(fields=['order', 'product'], name='order_produ_order_i_8825f6_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['department'], name='products_departm_a1d477_idx'),
        ),
        migrations.AddIndex(
            model_name='profit_by_hour',
            index=models.Index(fields=['hour_of_day'], name='profit_by_h_hour_of_402efd_idx'),
        ),
    ]
