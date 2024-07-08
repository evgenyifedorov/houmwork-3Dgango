# Generated by Django 5.0.6 on 2024-07-08 19:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_payment_total_sum_payment_payment_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователи",
            ),
        ),
    ]
