from django.shortcuts import render, HttpResponse

#from mantenimiento.models import Mantenimiento

# Create your views here.

def inicio(request):
    return render(request, 'BodegaInventarioApp/inicio.html')

#def mantenimiento(request):
#    mantenimientos = Mantenimiento.objects.all()
#    return render(request, 'BodegaInventarioApp/mantenimiento.html', {'mantenimientos': mantenimientos})

def transacciones(request):
    return render(request, 'BodegaInventarioApp/transacciones.html')

#def inventario(request):
#    return render(request, 'BodegaInventarioApp/inventario.html')

def reportes(request):
    return render(request, 'BodegaInventarioApp/reportes.html')