from django.urls import path
from FuncDashboard import views




urlpatterns = [
    path('func',views.FuncDashboard,name="FuncDashBoard"),
    path('func/logout/',views.logout_view,name="logout"),
    path('func/marcacao',views.marcacao_view,name="marcacao"),
    path('func/perfil',views.perfil_view,name="perfil"),
]