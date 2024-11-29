from django.urls import path
from producto_app import views

urlpatterns = [
    path('producto',views.inicio_vistaProducto,name="producto"),
    path("registrarProducto/", views.registrarProducto, name="registrarProducto"),
    path("borrarProduccto/<id_producto>",views.borrarProduccto, name="borrarProduccto"),
    path("seleccionarProducto/<id_producto>", views.seleccionarProducto, name="selecionarProducto"),
    path("editarProducto/", views.editarProducto, name="editarProducto")
]