from django.urls import path
from .views import IndexView, AutorView, AutorAPIxml, AutorAPIjson

urlpatterns = [
    # El parámetro name le asignamos un nombre para llamar a nuestra ruta
    # Así si cambiamos la ruta de "/" a hola/ el nombre seguira indicando la ruta
    path('', IndexView, name="IndexName"), # Ruta principal y cargamos Index
    path('autor/<int:id>', AutorView, name="AutorName"), # Indicamos que usaremos autor/ y un parametro int
    path('api/listado-autores-xml/', AutorAPIxml, name='autor_xml'),
    path('api/listado-autores-json/', AutorAPIjson, name='autor_json'),
]
