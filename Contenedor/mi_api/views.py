from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from App1.models import AutorDb, FraseDb
from .serializers import AutorDbSerializer, FraseDBSerializer, AutorConFraseSerializer

# Create your views here.
class AutorDbAPIList(generics.ListAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerializer


class AutorConFraseAPIList(generics.ListAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorConFraseSerializer


class AutorDbAPICreate(generics.CreateAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerializer


class AutorDbAPIRetrieve(generics.RetrieveAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerializer


# ViewSets
class FraseDBViewSet(viewsets.ModelViewSet):
    queryset = FraseDb.objects.all()
    serializer_class = FraseDBSerializer