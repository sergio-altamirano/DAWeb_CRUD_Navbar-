from django.urls import path
from sucursales_app import views

urlpatterns = [
    path('sucursal',views.inicio_vistaSucursal,name="sucursal"),
    path("registrarsucursal/", views.registrarSucursal, name="registrarsucursal"),
    path("borrarSucursal/<id_sucursal>",views.borrarSucursal, name="borrarSucursal"),
    path("seleccionarSucursal/<id_sucursal>", views.seleccionarSucursal, name="selecionarSucursal"),
    path("editarSucursal/", views.editarSucursal, name="editarSucursal")
]