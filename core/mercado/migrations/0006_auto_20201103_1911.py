# Generated by Django 2.2 on 2020-11-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0005_producto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=35),
        ),
    ]
