# Generated by Django 4.2.6 on 2024-01-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_remove_orders_buyer_remove_orders_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.IntegerField(),
        ),
    ]