from django.urls import path
from provedor_app import views

urlpatterns = [
    path('proovedor',views.inicio_vistaProovedor,name="proovedor"),
    path("registrarProvedor/", views.registrarProvedor, name="registrarProvedor"),
    path("borrarProvedor/<id_provedor>",views.borrarProvedor, name="borrarProvedor"),
    path("seleccionarProvedor/<id_provedor>", views.seleccionarProvedor, name="selecionarProvedor"),
    path("editarProvedor/", views.editarProvedor, name="editarProvedor")
]