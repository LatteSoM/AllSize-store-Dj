# Generated by Django 4.2.6 on 2023-12-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_goods_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='brands_pic',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='category',
            name='cat_pic',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
