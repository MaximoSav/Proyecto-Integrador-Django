# Generated by Django 2.2 on 2020-11-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0016_auto_20201125_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=100),
        ),
    ]
