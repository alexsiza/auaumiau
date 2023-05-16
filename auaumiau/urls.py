"""auaumiau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework import routers
from app.viewsets import PersonViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename="Person")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path("create_person", views.person_create, name='create_person'),
    path("read_person", views.person_read, name='read_person'),
    path("update_person/<int:id>", views.person_update, name='update_person'),
    path("delete_person/<int:id>", views.person_delete, name='delete_person'),
    path("update_doc/<int:id>", views.doc_update, name='update_doc'),
    path("delete_doc/<int:id>", views.doc_delete, name='delete_doc'),
    path('api/', include(router.urls)),
]