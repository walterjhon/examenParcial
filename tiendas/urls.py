from django.urls import path
from . import views

app_name = 'tiendas'
urlpatterns = [
    path('', views.index, name='index'),
    path('tienda', views.tienda, name='tienda')
]