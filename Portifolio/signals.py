from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from FuncDashboard.models import ServicosReservado

@receiver(post_save, sender=ServicosReservado)
def atualizar_total_reserva_apos_save(sender, instance, **kwargs):
    instance.reserva.atualizar_total()

@receiver(post_delete, sender=ServicosReservado)
def atualizar_total_reserva_apos_delete(sender, instance, **kwargs):
    instance.reserva.atualizar_total()