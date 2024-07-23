# Generated by Django 5.0.7 on 2024-07-23 18:16

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FuncDashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome Completo')),
                ('endereco', models.CharField(max_length=20, verbose_name='Endereço')),
                ('numero', phonenumber_field.modelfields.PhoneNumberField(max_length=9, region='AO', verbose_name='Número de Tel')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2, verbose_name='Genero')),
                ('dataNasc', models.DateField(verbose_name='Data de Nascimento')),
                ('img', models.ImageField(blank=True, null=True, upload_to='cli/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliUsuario', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.BooleanField()),
                ('data_entrada', models.DateField()),
                ('data_saida', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cli', to='Portifolio.cliente')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='func', to='FuncDashboard.funcionario')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido_loja', to='FuncDashboard.loja')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.IntegerField()),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servico', to='FuncDashboard.servico')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to='Portifolio.pedido')),
            ],
        ),
    ]
