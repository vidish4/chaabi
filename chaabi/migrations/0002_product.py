# Generated by Django 4.2.7 on 2023-11-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chaabi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("index", models.IntegerField()),
                ("product", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("sub_category", models.CharField(max_length=100)),
                ("brand", models.CharField(max_length=100)),
                ("sale_price", models.IntegerField()),
                ("market_price", models.IntegerField()),
                ("type", models.CharField(max_length=100)),
                ("rating", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=1000)),
            ],
        ),
    ]
