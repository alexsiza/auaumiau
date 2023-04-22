
from django.urls import path, include
from rest_framework import routers
from .viewsets import PersonViewSet
from . import views


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename="Person")



urlpatterns = [
    path("login", views.login, name='login'),
    path("agenda", views.area_de_agendamento, name='agenda'),
    path("", views.home, name='home'),
    path("servicos", views.servicos, name='servicos' ),
    path("farmacia", views.farmacia, name='farmacia'),
    path("cadastro", views.cadastro, name='cadastro'),
    path("serv", views.cadastro, name='serv'),
    path("pet", views.cadastro, name='pet'),

    path("create_person", views.person_create, name='create_person'),
    path("read_person", views.person_read, name='read_person'),
    path("update_person/<int:id>", views.person_update, name='update_person'),
    path("delete_person/<int:id>", views.person_delete, name='delete_person'),
    path('api/', include(router.urls)),
]


