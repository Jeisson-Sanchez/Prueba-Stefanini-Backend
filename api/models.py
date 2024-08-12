from django.db import models as mysql_models
from djongo import models as mongo_models

# Modelo MySql
class producto(mysql_models.Model):
    nombre = mysql_models.CharField(max_length=100)
    activo = mysql_models.BooleanField(default=True)

def __str__(self):
        return self.nombre

# Modelo  MongoDB
# class inventario(mongo_models.Model):
#     idInventario = mongo_models.IntegerField(unique=True)
#     nombreUsuario = mongo_models.CharField(max_length=100)
#     nombreProducto = mongo_models.CharField(max_length=100)
#     numSerie = mongo_models.IntegerField()
#     fechaCreate = mongo_models.DateField()
#     estado = mongo_models.BooleanField(default=True)
        
#     class Meta:
#         db_table = 'inventario' 
#         app_label = 'inventario'  

class inventario(mysql_models.Model):
    nombreUsuario = mysql_models.CharField(max_length=100)
    nombreProducto = mysql_models.CharField(max_length=100)
    numSerie = mysql_models.IntegerField()
    fechaCreate = mysql_models.DateField()
    estado = mysql_models.BooleanField(default=True)