# Generated by Django 4.2.7 on 2024-04-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_user_review_userview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='date_added',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='email',
            field=models.EmailField(max_length=10, null=True),
        ),
    ]
