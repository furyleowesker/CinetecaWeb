# Generated by Django 3.2.9 on 2021-11-30 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('idioma', models.CharField(max_length=255)),
                ('estreno', models.DateField()),
                ('duracion', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_sala', models.IntegerField()),
                ('numero_asientos', models.IntegerField()),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('dia', models.DateField()),
                ('pelicula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_venta.pelicula')),
                ('sala', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_venta.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_asiento', models.CharField(max_length=4)),
                ('precio', models.FloatField()),
                ('funcion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_venta.funcion')),
            ],
        ),
    ]
