from django.shortcuts import render, redirect
from .models import Trabajador

# Create your views here.

def inicio_vistaTrabajador(request):
    trabajador=Trabajador.objects.all()
    return render(request,'gestionartrabajador.html', {"mistrabajadores":trabajador})

def registrarTrabajador(request):
    id_trabajador=request.POST["txtid_trabajador"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    puesto=request.POST["txtpuesto"]
    fecha_nac=request.POST["txtfecha_nac"]
    curp=request.POST["txtcurp"]
    salario=request.POST["numsalario"]
    guardartrabajador=Trabajador.objects.create(id_trabajador=id_trabajador, nombre=nombre, apellido=apellido, puesto=puesto, fecha_nac=fecha_nac, curp=curp,salario=salario )
    return redirect('trabajador')

def seleccionarTrabajador(request,id_trabajador):
    trabajador=Trabajador.objects.get(id_trabajador=id_trabajador)
    return render(request,"editartrabajador.html", {"mistrabajadores":trabajador})

def borrarTrabajador(request,id_trabajador):
    trabajador=Trabajador.objects.get(id_trabajador=id_trabajador)
    trabajador.delete()
    return redirect('trabajador')

def editarTrabajador(request):
    id_trabajador=request.POST["txtid_trabajador"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    puesto=request.POST["txtpuesto"]
    fecha_nac=request.POST["txtfecha_nac"]
    curp=request.POST["txtcurp"]
    salario=request.POST["numsalario"]
    trabajador=Trabajador.objects.get(id_trabajador=id_trabajador)
    trabajador.id_trabajador=id_trabajador
    trabajador.nombre=nombre
    trabajador.apellido=apellido
    trabajador.puesto=puesto
    trabajador.fecha_nac=fecha_nac
    trabajador.curp=curp
    trabajador.salario=salario
    trabajador.save()
    return redirect('trabajador')