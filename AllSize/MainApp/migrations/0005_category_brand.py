# Generated by Django 4.2.6 on 2023-11-19 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_mainproducts_hugecard'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainApp.brands'),
            preserve_default=False,
        ),
    ]
