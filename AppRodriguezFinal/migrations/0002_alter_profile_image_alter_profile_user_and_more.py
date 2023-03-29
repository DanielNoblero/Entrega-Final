# Generated by Django 4.1.7 on 2023-03-29 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppRodriguezFinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='avatares', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Preparacion',
            field=models.TextField(max_length=5000),
        ),
    ]
