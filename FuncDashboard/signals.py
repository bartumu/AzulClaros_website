from django.dispatch import receiver
from .models import Sobre, Servico, MetodoPagamento
from django.db.models.signals import post_migrate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Reserva, ReservaEstatistica

@receiver(post_save, sender=Reserva)
def atualizar_estatisticas(sender, instance, created, **kwargs):
    # Obtém o mês e o ano da reserva
    mes = instance.data_reserva.replace(day=1)
    novo_estado = instance.estado
    func = instance.funcionario

    if created:
        # Caso a reserva tenha sido criada, incrementa a quantidade do estado correspondente
        estatistica, _ = ReservaEstatistica.objects.get_or_create(mes=mes, estado=novo_estado)
        estatistica.quantidade += 1
        estatistica.save()
    else:
        # Caso a reserva tenha sido editada, verifica se o estado foi alterado
        reserva_antiga = Reserva.objects.get(pk=instance.pk)
        if ReservaEstatistica.objects.filter(funcionario_id=func).exists():
            reserva_estati = ReservaEstatistica.objects.get(funcionario_id=func)
            reserva_estati.quantidade += 1
            reserva_estati.save()
            """ for res in reserva_estati:
                if res.mes == mes:
                    if res.estado == 1:
                        if res.funcionario == func:
                            reserva_estati.quantidade += 1
                            reserva_estati.save()
                            break
                    elif novo_estado == 1:
                        estatistica_nova, _ = ReservaEstatistica.objects.get_or_create(mes=mes, estado=novo_estado, funcionario=func)
                        estatistica_nova.quantidade += 1
                        estatistica_nova.save()
                        break

                if res.mes == mes:
                    if res.estado == 2: 
                        if res.funcionario == func:
                            reserva_estati.quantidade += 1
                            reserva_estati.save()
                            break
                    elif novo_estado == 2:
                        estatistica_nova, _ = ReservaEstatistica.objects.get_or_create(mes=mes, estado=novo_estado, funcionario=func)
                        estatistica_nova.quantidade += 1
                        estatistica_nova.save()
                        break """
        else:
            reserva_estati = ReservaEstatistica.objects.get(mes=mes, estado=novo_estado)
            reserva_estati.quantidade += 1
            reserva_estati.funcionario = func
            reserva_estati.save()
            """ for res in reserva_estati:
                if res.mes == mes:
                    if res.estado == 1:
                        print('Entrou')
                        reserva_estati.quantidade += 1
                        reserva_estati.funcionario = func
                        reserva_estati.save()
                        break
                    elif novo_estado == 1:
                        estatistica_nova, _ = ReservaEstatistica.objects.get_or_create(mes=mes, estado=novo_estado, funcionario=func)
                        estatistica_nova.quantidade += 1
                        estatistica_nova.save()
                        break

                if res.mes == mes:
                    if res.estado == 2: 
                        reserva_estati.quantidade += 1
                        reserva_estati.funcionario = func
                        reserva_estati.save()
                        break
                    elif novo_estado == 2:
                        estatistica_nova, _ = ReservaEstatistica.objects.get_or_create(mes=mes, estado=novo_estado, funcionario=func)
                        estatistica_nova.quantidade += 1
                        estatistica_nova.save()
                        break """

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'FuncDashboard':
        if not MetodoPagamento.objects.exists():
            
            MetodoPagamento.objects.create(
                metodo='Dinheiro',
            )

            MetodoPagamento.objects.create(
                metodo='Cartão',
            )

        if not Sobre.objects.exists():
            sobre_texto = ("Somos uma lavandaria com um sistema totalmente diferenciado no mercado angolano, "
                           "a maior parte das lavandarias no país, o que elas fazem não é serviço de lavandaria, "
                           "mas de tinturaria, Pois oferecemos serviços de lavagem, secagem e engomagem de forma "
                           "conjunta bem como segregada, por intermédio de cestos de roupas tu consegues fazer a "
                           "lavagem, secagem ou engomagem de suas roupas em nossas lavandaria. Aqui a lavagem é "
                           "feita em quantidade, pois acreditamos que o custo de lavagem de produção de uma única "
                           "lavagem é o mesmo em quantidade.")
            Sobre.objects.create(
                titulo='Sobre a Empresa',
                descricao=sobre_texto
            )

        if not Servico.objects.exists():
            Servico.objects.create(
                nome='Lavagem Completa',
                descricao='Serviço de lavagem completa de roupas.',
                preco=3500,
                img=None  # ou coloque o caminho da imagem se tiver uma
            )
            Servico.objects.create(
                nome='Secagem',
                descricao='Serviço de secagem de roupas.',
                preco=2000,
                img=None  # ou coloque o caminho da imagem se tiver uma
            )
            Servico.objects.create(
                nome='Engomagem',
                descricao='Serviço de engomagem de roupas.',
                preco=2500,
                img=None  # ou coloque o caminho da imagem se tiver uma
            )