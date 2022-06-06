from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Pago
from inscripciones.models import Inscripcion
from socios.models import Socio

class PagoAdmin(admin.ModelAdmin):
    # list_display = ['actividad', 'socio', 'fechapago', 'show']
    list_display = ['fechapago', 'comprobante', 'actividad', 'socio', 'dni_socio']
    # def show(seld, obj):
        # return mark_safe(f'<a href="www.google.com/{obj.id}"> Google </a>')
    autocomplete_fields = ['socio']
    # search_fields = ['fechapago', 'inscripcion__socio__dni', 'inscripcion__socio__nombre', 'inscripcion__socio__apellido']

    # def nombre_socio(self, obj):
    #     inscripcion = Inscripcion.objects.get(id = obj.inscripcion.id)
    #     return inscripcion.socio

    def dni_socio(self, obj):
        socio = Socio.objects.get(id = obj.socio.id)
        return socio.dni

admin.site.register(Pago, PagoAdmin)
