# Generated by Django 5.1 on 2024-09-01 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FuncDashboard', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservaestatistica',
            unique_together={('mes', 'estado', 'funcionario')},
        ),
    ]
