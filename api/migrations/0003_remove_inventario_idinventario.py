# Generated by Django 4.1.13 on 2024-08-12 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_inventario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='idInventario',
        ),
    ]
