# Generated by Django 4.2.7 on 2023-11-12 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("phone", models.CharField(default="+79999999999", max_length=20)),
                ("is_banned", models.BooleanField(default=False)),
                (
                    "img",
                    models.ImageField(
                        blank=True,
                        default="ava.png",
                        null=True,
                        upload_to="product",
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
