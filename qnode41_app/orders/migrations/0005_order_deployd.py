# Generated by Django 3.2.5 on 2021-10-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_ci'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deployd',
            field=models.BooleanField(default=False),
        ),
    ]
