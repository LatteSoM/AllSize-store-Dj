# Generated by Django 4.2.6 on 2023-12-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_category_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
