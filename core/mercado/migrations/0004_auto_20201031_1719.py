# Generated by Django 2.2 on 2020-10-31 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0003_auto_20201031_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercado.Direccion'),
        ),
    ]
