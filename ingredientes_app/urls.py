from django.urls import path
from ingredientes_app import views

urlpatterns = [
    path('ingredientes',views.inicio_vistaIngredientes,name="ingredientes"),
    path("registrarIngrediente/", views.registrarIngrediente, name="registrarIngrediente"),
    path("borrarIngrediente/<id_ingrediente>",views.borrarIngrediente, name="borrarIngrediente"),
    path("seleccionarIngrediente/<id_ingrediente>", views.seleccionarIngrediente, name="selecionarIngrediente"),
    path("editarIngrediente/", views.editarIngrediente, name="editarIngrediente")
]