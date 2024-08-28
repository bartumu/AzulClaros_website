from django.urls import path
from . import views




urlpatterns = [
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('recuperar/',views.recuperar_view,name="recuperarSenha"),
    path('recuperar/senha/',views.recuperar_senha,name="reporSenha"),
]