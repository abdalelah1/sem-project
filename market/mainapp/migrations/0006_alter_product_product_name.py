# Generated by Django 4.1.5 on 2023-03-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_product_product_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_name',
            field=models.CharField(max_length=1000),
        ),
    ]
