# Generated by Django 5.0.8 on 2024-08-12 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FuncDashboard', '0004_alter_servico_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='reserva',
        ),
    ]
