# Generated by Django 4.2.7 on 2023-11-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chaabi", "0002_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="vector",
            field=models.CharField(default=None, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="index",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="product",
            name="market_price",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="product",
            name="sale_price",
            field=models.CharField(max_length=100),
        ),
    ]