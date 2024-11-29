from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.

def inicio_vistaSucursal(request):
    sucursal=Sucursal.objects.all()
    return render(request,'gestionarsucursal.html', {"missucursal":sucursal})

def registrarSucursal(request):
    id_sucursal=request.POST["numid_sucursal"]
    horario=request.POST["txthorario"]
    num_trabajadores=request.POST["txtnum_trabajadores"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    id_ventas=request.POST["txtid_ventas"]
    correo=request.POST["txtcorreo"]
    guardarsucursal=Sucursal.objects.create(id_sucursal=id_sucursal, horario=horario, num_trabajadores=num_trabajadores, direccion=direccion, telefono=telefono, id_ventas=id_ventas,correo=correo )
    return redirect('sucursal')

def seleccionarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request,"editarsucursal.html", {"missucursal":sucursal})

def borrarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect('sucursal')

def editarSucursal(request):
    id_sucursal=request.POST["numid_sucursal"]
    horario=request.POST["txthorario"]
    num_trabajadores=request.POST["txtnum_trabajadores"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    id_ventas=request.POST["txtid_ventas"]
    correo=request.POST["txtcorreo"]
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.id_sucursal=id_sucursal
    sucursal.horario=horario
    sucursal.num_trabajadores=num_trabajadores
    sucursal.direccion=direccion
    sucursal.telefono=telefono
    sucursal.id_ventas=id_ventas
    sucursal.correo=correo
    sucursal.save()
    return redirect('sucursal')