# Generated by Django 5.1.2 on 2024-10-20 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')], default='abierto', max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('mensaje', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chatbot.mensaje')),
            ],
        ),
        migrations.AddField(
            model_name='mensaje',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.usuario'),
        ),
    ]
