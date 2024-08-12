# Generated by Django 4.1.13 on 2024-08-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idInventario', models.IntegerField(unique=True)),
                ('nombreUsuario', models.CharField(max_length=100)),
                ('nombreProducto', models.CharField(max_length=100)),
                ('numSerie', models.IntegerField()),
                ('fechaCreate', models.DateField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
