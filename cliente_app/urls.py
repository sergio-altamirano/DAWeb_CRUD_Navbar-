from django.urls import path
from cliente_app import views

urlpatterns = [
    path('cliente',views.inicio_vistaCliente,name="cliente"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("borrarCliente/<id_cliente>",views.borrarCliente, name="borrarCliente"),
    path("seleccionarCliente/<id_cliente>", views.seleccionarCliente, name="selecionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente")
]