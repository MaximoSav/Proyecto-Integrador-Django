# Generated by Django 2.2 on 2020-11-25 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0014_auto_20201125_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='direccion',
        ),
    ]
