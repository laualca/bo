from django.shortcuts import render, redirect
from mantenimiento.models import Mantenimiento
from django.contrib import messages

# Create your views here.
def mantenimiento(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'mantenimiento/mantenimiento.html', {'mantenimientos': mantenimientos})

def guardar(request):
    titulo = request.POST['titulo']
    descripcion = request.POST['descripcion']
    fecha_mante = request.POST['fecha_mante']
    responsable_mante = request.POST['responsable_mante']
    p = Mantenimiento(titulo=titulo, descripcion=descripcion, fecha_mante=fecha_mante, responsable_mante=responsable_mante)
    p.save()
    messages.success(request, 'Mantenimiento guardado correctamente')
    return redirect('mantenimiento')  # Redirigir a la vista de mantenimiento

def eliminar(request, id_mantenimiento):
    p = Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
    p.delete()
    messages.success(request, 'Mantenimiento eliminado correctamente')
    return redirect('mantenimiento')  # Redirigir a la vista de mantenimiento

def editar(request, id_mantenimiento):
    p = Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
    return render(request, 'mantenimiento/editar.html', {'mantenimiento': p})
