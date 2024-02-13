from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import AutorDb, FraseDb
#from django.http import HttpResponse

# Create your views here.
def IndexView(request):
    '''Esto es la página principal'''

    # Solicitamos los objetos a la base de datos y los ordenamos del último al primero
    objeto = AutorDb.objects.all().order_by("-id") 

    # retornamos una http con la plantilla index.html y los objetos de la base de datos
    return render(request, "index.html", {"objeto":objeto})

def AutorView(request, id):
    # Solicitamos un objeto a la base de datos y si no existe elevamos un 404
    autor = get_object_or_404(AutorDb, id=id)

    # retornamos una http con la plantilla autor.html y el objeto de la base de datos
    return render(request, "autor.html", {"objeto":autor})


# Vistas API

def AutorAPIxml(request):
    autores = AutorDb.objects.all()
    autores_serializados = serialize('xml', autores)
    return HttpResponse(autores_serializados, content_type='text/xml')


def AutorAPIjson(request):
    autores = AutorDb.objects.all()
    autores_serializados = serialize('json', autores)
    return HttpResponse(autores_serializados, content_type='text/json')