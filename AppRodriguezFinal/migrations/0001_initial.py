# Generated by Django 4.1.7 on 2023-03-28 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_de_receta', models.CharField(max_length=30)),
                ('Autor', models.CharField(max_length=15)),
                ('Rendimiento', models.CharField(max_length=10)),
                ('Horas_de_prepracion', models.CharField(max_length=50)),
            ],
        ),
    ]
