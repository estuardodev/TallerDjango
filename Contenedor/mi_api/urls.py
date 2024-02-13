from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AutorDbAPIList,
    AutorDbAPICreate,
    AutorDbAPIRetrieve,
    AutorConFraseAPIList,
    FraseDBViewSet
)

router = DefaultRouter()
router.register('frases', FraseDBViewSet, basename='frases')

urlpatterns = [
    path('autores-list/', AutorDbAPIList.as_view(), name='autores_list'),
    path('autores-frases/', AutorConFraseAPIList.as_view(), name='autor_frase'),
    path('autores-create/', AutorDbAPICreate.as_view(), name='autores_create'),
    path('autores-retrieve/<int:pk>/', AutorDbAPIRetrieve.as_view(), name='autores_retrieve')
]

urlpatterns += router.urls 