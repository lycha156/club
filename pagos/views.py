from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from inscripciones.models import Inscripcion
from actividades.models import Actividad
from socios.models import Socio
from .models import Pago

def pagos_create(request, id):
    socio = Socio.objects.get(id = id)
    inscripciones = Inscripcion.objects.filter(socio_id = id)
    context = {
        'socio': socio,
        'inscripciones': inscripciones
    }
    return render(request, 'pagos_create.html', context)

def pagos_create_save(request):
    if request.method == 'POST':
        pago = Pago()
        socio = Socio.objects.get(id = request.POST.get('socio_id'))
        inscripcion = Inscripcion.objects.get(id = request.POST.get('inscripcion_id'))
        pago.socio = socio
        pago.actividad = inscripcion.actividad.actividad
        pago.fechapago = request.POST.get('fechapago')
        pago.comprobante = request.POST.get('comprobante')
        pago.save()
        return redirect('admin:index')
    else:
        return HttpResponse('asdasd')
