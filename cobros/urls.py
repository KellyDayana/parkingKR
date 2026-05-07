from django.urls import path
from . import views

app_name = 'cobros'

urlpatterns = [
    # Cliente CRUD
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.cliente_delete, name='cliente_delete'),

    # Espacios y pagos
    path('espacios/libres/', views.espacios_libres, name='espacios_libres'),
    path('pagos/activos/', views.pagos_activos, name='pagos_activos'),

    # Flujo parqueo
    path('ingreso/', views.registrar_ingreso, name='registrar_ingreso'),
    path('salida/', views.registrar_salida, name='registrar_salida'),
]