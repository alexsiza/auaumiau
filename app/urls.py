
from django.urls import path, include
from rest_framework import routers
from .viewsets import PersonViewSet
from . import views


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename="Person")



urlpatterns = [
    path("login", views.login, name='login'),
    path("agenda", views.agenda, name='agenda'),
    path("home", views.home, name='home'),
    path("servicos", views.servicos, name='servicos' ),
    path("farmacia", views.farmacia, name='farmacia'),
    path("cadastro", views.cadastro, name='cadastro'),
    path("name", views.name, name='name'),
    path("agenda2", views.agenda2, name='agenda2'),
    path("serv", views.serv, name='serv'),
    path("serv2", views.serv2, name='serv2'),
    path("pet", views.pet, name='pet'),

    path("create_person", views.person_create, name='create_person'),
    path("read_person", views.person_read, name='read_person'),
    path("update_person/<int:id>", views.person_update, name='update_person'),
    path("delete_person/<int:id>", views.person_delete, name='delete_person'),
    path('api/', include(router.urls)),
]


