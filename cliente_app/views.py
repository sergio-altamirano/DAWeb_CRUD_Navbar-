from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def inicio_vistaCliente(request):
    cliente=Cliente.objects.all()
    return render(request,'gestionarCliente.html', {"misclientes":cliente})

def registrarCliente(request):
    id_cliente=request.POST["numid_cliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    telefono=request.POST["txttelefono"]
    fecha_nac=request.POST["txtfecha_nac"]
    domicilio=request.POST["txtdomicilio"]
    curp=request.POST["numcurp"]
    guardarcliente=Cliente.objects.create(id_cliente=id_cliente, nombre=nombre, apellido=apellido, telefono=telefono, fecha_nac=fecha_nac, domicilio=domicilio, curp=curp)
    return redirect('cliente')

def seleccionarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarCliente.html", {"misclientes":cliente})

def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect('cliente')

def editarCliente(request):
    id_cliente=request.POST["numid_cliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    telefono=request.POST["txttelefono"]
    fecha_nac=request.POST["txtfecha_nac"]
    domicilio=request.POST["txtdomicilio"]
    curp=request.POST["numcurp"]
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.telefono=telefono
    cliente.fecha_nac=fecha_nac
    cliente.domicilio=domicilio
    cliente.curp=curp
    cliente.save()
    return redirect('cliente')