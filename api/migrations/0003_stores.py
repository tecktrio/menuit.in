# Generated by Django 5.0.2 on 2024-03-10 03:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_division_division_store_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('store_license_number', models.CharField(max_length=50)),
                ('store_rating', models.IntegerField(default=5)),
                ('store_desription', models.TextField()),
                ('store_image_url', models.TextField()),
                ('store_open_dates', models.IntegerField(default=0)),
                ('store_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shopowners')),
            ],
            options={
                'verbose_name_plural': 'Stores',
            },
        ),
    ]