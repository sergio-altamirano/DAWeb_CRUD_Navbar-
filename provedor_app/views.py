from django.shortcuts import render, redirect
from .models import Provedor

# Create your views here.

def inicio_vistaProovedor(request):
    provedor=Provedor.objects.all()
    return render(request,'gestionarprovedor.html', {"misprovedor":provedor})

def registrarProvedor(request):
    id_provedor=request.POST["numid_provedor"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    tipo_entrega=request.POST["txttipo_entrega"]
    dia_entrega=request.POST["txtdia_entrega"]
    guardarprovedor=Provedor.objects.create(id_provedor=id_provedor, nombre=nombre, direccion=direccion, telefono=telefono, correo=correo, tipo_entrega=tipo_entrega, dia_entrega=dia_entrega)
    return redirect('proovedor')

def seleccionarProvedor(request,id_provedor):
    provedor=Provedor.objects.get(id_provedor=id_provedor)
    return render(request,"editarprovedor.html", {"misprovedor":provedor})

def borrarProvedor(request,id_provedor):
    provedor=Provedor.objects.get(id_provedor=id_provedor)
    provedor.delete()
    return redirect('proovedor')

def editarProvedor(request):
    id_provedor=request.POST["numid_provedor"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    tipo_entrega=request.POST["txttipo_entrega"]
    dia_entrega=request.POST["txtdia_entrega"]
    provedor=Provedor.objects.get(id_provedor=id_provedor)
    provedor.id_provedor=id_provedor
    provedor.nombre=nombre
    provedor.direccion=direccion
    provedor.telefono=telefono
    provedor.correo=correo
    provedor.tipo_entrega=tipo_entrega
    provedor.dia_entrega=dia_entrega
    provedor.save()
    return redirect('proovedor')