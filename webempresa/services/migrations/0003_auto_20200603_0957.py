# Generated by Django 3.0.6 on 2020-06-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200602_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-Created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AlterField(
            model_name='service',
            name='Created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Subtitle',
            field=models.CharField(max_length=200, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]
