from django.shortcuts import render
from inventario.models import Inventario

# Create your views here.
def inventario(request):
    
    inventario = Inventario.objects.all()
    #return render(request, 'BodegaInventarioApp/inventario.html')
    return render(request, 'inventario/inventario.html', {"inventario":inventario})

