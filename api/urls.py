from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'inventarios', views.InventarioViewSet)

urlpatterns = [
    path('', include(router.urls))
]