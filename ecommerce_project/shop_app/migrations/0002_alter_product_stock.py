# Generated by Django 5.0.6 on 2024-07-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
