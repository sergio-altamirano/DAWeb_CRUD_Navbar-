from django.shortcuts import render, redirect
from .models import Ingrediente

# Create your views here.

def inicio_vistaIngredientes(request):
    ingrediente=Ingrediente.objects.all()
    return render(request,'gestionaringrediente.html', {"misingrediente":ingrediente})

def registrarIngrediente(request):
    id_ingrediente=request.POST["numid_ingrediente"]
    id_provedor=request.POST["txtid_provedor"]
    id_producto=request.POST["txtid_producto"]
    tipo_carne=request.POST["txttipo_carne"]
    id_categoria=request.POST["txtid_categoria"]
    guardaringrediente=Ingrediente.objects.create(id_ingrediente=id_ingrediente, id_provedor=id_provedor, id_producto=id_producto, tipo_carne=tipo_carne, id_categoria=id_categoria)
    return redirect('ingredientes')

def seleccionarIngrediente(request,id_ingrediente):
    ingrediente=Ingrediente.objects.get(id_ingrediente=id_ingrediente)
    return render(request,"editaringrediente.html", {"misingrediente":ingrediente})

def borrarIngrediente(request,id_ingrediente):
    ingrediente=Ingrediente.objects.get(id_ingrediente=id_ingrediente)
    ingrediente.delete()
    return redirect('ingredientes')

def editarIngrediente(request):
    id_ingrediente=request.POST["numid_ingrediente"]
    id_provedor=request.POST["txtid_provedor"]
    id_producto=request.POST["txtid_producto"]
    tipo_carne=request.POST["txttipo_carne"]
    id_categoria=request.POST["txtid_categoria"]
    ingrediente=Ingrediente.objects.get(id_ingrediente=id_ingrediente)
    ingrediente.id_ingrediente=id_ingrediente
    ingrediente.id_provedor=id_provedor
    ingrediente.id_producto=id_producto
    ingrediente.tipo_carne=tipo_carne
    ingrediente.id_categoria=id_categoria
    ingrediente.save()
    return redirect('ingredientes')