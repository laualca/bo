from django.shortcuts import render, redirect
from mantenimiento.models import Mantenimiento

# Create your views here.
def mantenimiento(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'mantenimiento/mantenimiento.html', {'mantenimientos': mantenimientos})

