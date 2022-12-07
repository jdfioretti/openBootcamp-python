# Generated by Django 4.1.3 on 2022-11-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Nombre del director', max_length=64)),
                ('apellido', models.CharField(default='Apellido del director', max_length=64)),
                ('titulo', models.CharField(help_text='Escriba el Titulo de la pelicula aqui', max_length=64)),
                ('descipcion', models.TextField(help_text='Escriba la descripcion de la pelicula aqui')),
            ],
        ),
    ]