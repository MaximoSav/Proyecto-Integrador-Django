# Generated by Django 2.2 on 2020-11-22 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0011_remove_producto_destacado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destacado',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mercado.Producto')),
            ],
        ),
    ]
