# Generated by Django 5.0.2 on 2024-03-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.IntegerField(),
        ),
    ]