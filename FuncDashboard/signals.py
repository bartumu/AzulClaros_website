from django.dispatch import receiver
from .models import Sobre, Servico, MetodoPagamento
from django.db.models.signals import post_migrate

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