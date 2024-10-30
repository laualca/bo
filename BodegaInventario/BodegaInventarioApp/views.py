from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'BodegaInventarioApp/inicio.html')

def mantenimiento(request):
    return render(request, 'BodegaInventarioApp/mantenimiento.html')

def transacciones(request):
    return render(request, 'BodegaInventarioApp/transacciones.html')



def reportes(request):
    return render(request, 'BodegaInventarioApp/reportes.html')