from django.urls import path
from trabajador_app import views

urlpatterns = [
    path('trabajador',views.inicio_vistaTrabajador,name="trabajador"),
    path("registrarTrabajador/", views.registrarTrabajador, name="registrarTrabajador"),
    path("borrarTrabajador/<id_trabajador>",views.borrarTrabajador, name="borrarTrabajador"),
    path("seleccionarTrabajador/<id_trabajador>", views.seleccionarTrabajador, name="selecionarTrabajador"),
    path("editarTrabajador/", views.editarTrabajador, name="editarTrabajador")
]