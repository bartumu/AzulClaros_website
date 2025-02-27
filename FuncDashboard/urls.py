from django.urls import path
from FuncDashboard import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('func',views.FuncDashboard,name="FuncDashBoard"),
    path('func/logout/',views.logout_view,name="logout"),
    path('func/Reserva',views.listReserva_view,name="reserva"),
    path('func/reserva/<int:idReserva>',views.atender_view,name="atender"),
    path('func/reservaLev',views.Levantamento_view,name="levantamento"),
    path('func/levantar/<int:idReserva>',views.levantar_view,name="Levantar"),
    path('func/perfil',views.RegistarPerfil,name="perfil"),
    path('func/Regperfil',views.RegistarPerfil,name="Regperfil"),
    path('func/Cliente',views.RegistarCliente,name="RegCliente"),
    path('Func/gerarPDF/<int:idReserva>',views.gerarPDF,name="gerarFactPDF"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)