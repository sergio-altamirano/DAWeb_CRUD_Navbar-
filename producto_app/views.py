from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def inicio_vistaProducto(request):
    producto=Producto.objects.all()
    return render(request,'gestionarProducto.html', {"misproductos":producto})

def registrarProducto(request):
    id_producto=request.POST["numid_producto"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["txtprecio"]
    cantidad=request.POST["txtacantidad"]
    id_ingrediente=request.POST["txtaid_ingrediente"]
    id_sucursal=request.POST["txtid_sucursal"]
    Id_categoria=request.POST["numId_categoria"]
    guardarproducto=Producto.objects.create(id_producto=id_producto, nombre=nombre, precio=precio, cantidad=cantidad, id_ingrediente=id_ingrediente, id_sucursal=id_sucursal, Id_categoria=Id_categoria)
    return redirect('producto')

def seleccionarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    return render(request,"editarProducto.html", {"misproductos":producto})

def borrarProduccto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect('producto')

def editarProducto(request):
    id_producto=request.POST["numid_producto"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["txtprecio"]
    cantidad=request.POST["txtacantidad"]
    id_ingrediente=request.POST["txtaid_ingrediente"]
    id_sucursal=request.POST["txtid_sucursal"]
    Id_categoria=request.POST["numId_categoria"]
    producto=Producto.objects.get(id_producto=id_producto)
    producto.id_producto=id_producto
    producto.nombre=nombre
    producto.precio=precio
    producto.cantidad=cantidad
    producto.id_ingrediente=id_ingrediente
    producto.id_sucursal=id_sucursal
    producto.Id_categoria=Id_categoria
    producto.save()
    return redirect('producto')