from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductoSerializer, InventarioSerializer
from .models import producto, inventario
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer
    
class InventarioViewSet(viewsets.ModelViewSet):
    queryset = inventario.objects.all()
    serializer_class = InventarioSerializer