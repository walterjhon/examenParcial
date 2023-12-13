from django.urls import path
from . import views
from .views import gestion_tiendas, gestion_productos, tienda_detalle

app_name = 'gestionTienda'

urlpatterns = [
    path('gestionTienda/', gestion_tiendas, name='gestion_tiendas'),
    path('gestionTienda/Productos/', gestion_productos, name='gestion_productos'),
    path('gestionTienda/Tienda/<int:tienda_id>/', tienda_detalle, name='tienda_detalle'),

]