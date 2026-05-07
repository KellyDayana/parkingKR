from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from .models import Cliente, Espacio, Pago

# Cliente CRUD
def cliente_list(request):
    clientes = list(Cliente.objects.values())
    return JsonResponse(clientes, safe=False)

@csrf_exempt
def cliente_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cliente = Cliente.objects.create(
            identificacion=data['identificacion'],
            nombre=data['nombre'],
            apellido=data['apellido'],
            telefono=data['telefono']
        )
        return JsonResponse({'id': cliente.id, 'message': 'Cliente creado'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def cliente_update(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
        if request.method == 'POST':
            data = json.loads(request.body)
            cliente.identificacion = data.get('identificacion', cliente.identificacion)
            cliente.nombre = data.get('nombre', cliente.nombre)
            cliente.apellido = data.get('apellido', cliente.apellido)
            cliente.telefono = data.get('telefono', cliente.telefono)
            cliente.save()
            return JsonResponse({'message': 'Cliente actualizado'})
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

@csrf_exempt
def cliente_delete(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
        if request.method == 'DELETE':
            cliente.delete()
            return JsonResponse({'message': 'Cliente eliminado'})
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

# Espacios libres
def espacios_libres(request):
    espacios = list(Espacio.objects.filter(ocupado=False).values('numero'))
    return JsonResponse(espacios, safe=False)

# Pagos activos (espacios ocupados)
def pagos_activos(request):
    pagos = list(Pago.objects.filter(fecha_salida__isnull=True).values(
        'id', 'cliente__nombre', 'cliente__apellido', 'espacio__numero', 'fecha_ingreso'
    ))
    return JsonResponse(pagos, safe=False)

# Registrar ingreso
@csrf_exempt
def registrar_ingreso(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cliente_id = data['cliente_id']
        espacio_numero = data['espacio_numero']
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            espacio = Espacio.objects.get(numero=espacio_numero, ocupado=False)
            espacio.ocupado = True
            espacio.save()
            pago = Pago.objects.create(cliente=cliente, espacio=espacio)
            return JsonResponse({'pago_id': pago.id, 'message': 'Ingreso registrado'})
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
        except Espacio.DoesNotExist:
            return JsonResponse({'error': 'Espacio no disponible'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Registrar salida
@csrf_exempt
def registrar_salida(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pago_id = data['pago_id']
        try:
            pago = Pago.objects.get(id=pago_id, fecha_salida__isnull=True)
            pago.fecha_salida = timezone.now()
            # Calcular valor (ejemplo: $2 por hora)
            duracion = pago.fecha_salida - pago.fecha_ingreso
            horas = duracion.total_seconds() / 3600
            pago.valor = round(horas * 2, 2)  # $2 por hora
            pago.save()
            pago.espacio.ocupado = False
            pago.espacio.save()
            return JsonResponse({'valor': str(pago.valor), 'message': 'Salida registrada'})
        except Pago.DoesNotExist:
            return JsonResponse({'error': 'Pago no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

