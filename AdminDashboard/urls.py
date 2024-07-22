from django.urls import path
from AdminDashboard import views




urlpatterns = [
    path('func',views.cliDashboard,name="cliDashBoard"),
    path('func/logout/',views.logout_view,name="logout"),
]