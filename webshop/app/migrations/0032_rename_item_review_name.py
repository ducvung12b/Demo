# Generated by Django 4.2.7 on 2024-06-29 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_order_all_product_remove_order_id_man_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='item',
            new_name='name',
        ),
    ]
