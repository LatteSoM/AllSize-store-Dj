# Generated by Django 4.2.6 on 2023-12-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_goods_articul'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='size',
            field=models.ManyToManyField(through='MainApp.SizesToGoodTable', to='MainApp.sizes'),
        ),
    ]
