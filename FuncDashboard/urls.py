from django.urls import path
from FuncDashboard import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('func',views.FuncDashboard,name="FuncDashBoard"),
    path('func/logout/',views.logout_view,name="logout"),
    path('func/marcacao',views.marcacao_view,name="marcacao"),
    path('func/marcacao/<int:idReserva>',views.atender_view,name="atender"),
    path('func/perfil',views.perfil_view,name="perfil"),
    path('func/Regperfil',views.RegistarPerfil,name="Regperfil"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)