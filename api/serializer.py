from rest_framework import serializers
from djongo import models as mongo_models
from .models import producto, inventario
from bson import ObjectId
   
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__' 
        
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventario
        # fields = ('idInventario','nombreUsuario','nombreProducto','numSerie','fechaCreate','estado')
        fields = '__all__' 