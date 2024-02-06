from django.urls import path
from .views import IndexView, AutorView

urlpatterns = [
    # El parámetro name le asignamos un nombre para llamar a nuestra ruta
    # Así si cambiamos la ruta de "/" a hola/ el nombre seguira indicando la ruta
    path('', IndexView, name="IndexName"), # Ruta principal y cargamos Index
    path('autor/<int:id>', AutorView, name="AutorName") # Indicamos que usaremos autor/ y un parametro int
]
