

from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name='login'),
    path("area_de_agendamento", views.area_de_agendamento, name='area_de_agendamento'),
    path("home", views.home, name='home'),
    path("servicos", views.servicos, name='servicos' ),
    path("farmacia", views.farmacia, name='farmacia'),
]


