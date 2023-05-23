# Generated by Django 4.0.4 on 2023-04-25 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_remove_orders_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_rating',
            name='product_rating_customer_fk',
        ),
        migrations.AlterField(
            model_name='shippinginfo',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customers'),
        ),
    ]
