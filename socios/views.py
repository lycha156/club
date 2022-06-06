from django.shortcuts import render
from django.http import HttpResponse
from .models import Socio
from inscripciones.models import Inscripcion
from pagos.models import Pago

def show(request, id):
    socio = Socio.objects.get(id=id)
    inscripciones = Inscripcion.objects.filter(socio_id = id)
    # insc_id = []
    # for i in inscripciones:
    #     insc_id.append(i.id)
    # pagos = Pago.objects.filter( inscripcion_id__in = insc_id)
    pagos = Pago.objects.filter(socio_id = id)
    context = {
        'socio': socio,
        'inscripciones': inscripciones,
        'pagos': pagos
    }
    return render(request, 'socios_show.html', context)

# BUSCAR SOCIO A COMPROBAR
def comprobar(request):
    return render(request, 'socios_comprobar.html')

# MOSTRAR DATOS DEL SOCIO
def socios_estado(request):
    try:
        dni = request.POST.get('dni')
        socio = Socio.objects.get(dni=dni)
        inscripciones = Inscripcion.objects.filter(socio_id = socio.id)
        # insc_id = []
        # for i in inscripciones:
        #     insc_id.append(i.id)
        # pagos = Pago.objects.filter( inscripcion_id__in = insc_id).order_by('-fechapago')[:10]
        pagos = Pago.objects.filter(socio_id = socio.id).order_by('-fechapago')[:10]
        context = {
            'socio': socio,
            'inscripciones': inscripciones,
            'pagos': pagos
        }

        return render(request, 'socios_estado.html', context)  
    except:
        context = {
            'mensaje': 'No es posible encontrar al socio soliciato.'
        }
        return render( request, 'socios_comprobar.html', context)
