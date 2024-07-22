from django.urls import path
from . import views




urlpatterns = [
    path('registar/',views.registar_view,name="registar"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
]