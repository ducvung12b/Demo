# Generated by Django 4.2.7 on 2024-05-18 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_order_item_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='item_product',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
