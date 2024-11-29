from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.

def inicio_vistaVentas(request):
    ventas=Ventas.objects.all()
    return render(request,'gestionarventas.html', {"misventas":ventas})

def registrarVentas(request):
    id_venta=request.POST["numid_venta"]
    id_producto=request.POST["numid_producto"]
    id_cliente=request.POST["numid_cliente"]
    fecha_venta=request.POST["txtfecha_venta"]
    id_sucursal=request.POST["numid_sucursal"]
    cantidad=request.POST["numcantidad"]
    pago=request.POST["txtpago"]
    guardarVentas=Ventas.objects.create(id_venta=id_venta, id_producto=id_producto, id_cliente=id_cliente, fecha_venta=fecha_venta, id_sucursal=id_sucursal, cantidad=cantidad,pago=pago )
    return redirect('ventas')

def seleccionarVentas(request,id_venta):
    ventas=Ventas.objects.get(id_venta=id_venta)
    return render(request,"editarventas.html", {"misventas":ventas})

def borrarVentas(request,id_venta):
    ventas=Ventas.objects.get(id_venta=id_venta)
    ventas.delete()
    return redirect('ventas')

def editarVentas(request):
    id_venta=request.POST["numid_venta"]
    id_producto=request.POST["numid_producto"]
    id_cliente=request.POST["numid_cliente"]
    fecha_venta=request.POST["txtfecha_venta"]
    id_sucursal=request.POST["numid_sucursal"]
    cantidad=request.POST["numcantidad"]
    pago=request.POST["txtpago"]
    ventas=Ventas.objects.get(id_venta=id_venta)
    ventas.id_producto=id_producto
    ventas.id_cliente=id_cliente
    ventas.fecha_venta=fecha_venta
    ventas.id_sucursal=id_sucursal
    ventas.cantidad=cantidad
    ventas.pago=pago
    ventas.save()
    return redirect('ventas')