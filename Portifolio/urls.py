from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('',views.index,name="home"),
    path('sobre',views.sobre,name="sobreNos"),
    path('reservas',views.reserva,name="reservaConsultar"),
    path('reservas/add',views.addReserva_view,name="reservaAdd"),
    path('reservas/gerarPDF/<int:idReserva>',views.gerarPDF,name="gerarPDF"),
    path('buscar_reserva', views.buscar_reserva, name='buscar_reserva'),
    path('NossoServicos/', views.servico, name='nossoServico'),
    path('Contacto/', views.contacto, name='contacto'),
] + static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)