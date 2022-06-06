from django.contrib import admin
from django.utils.safestring import mark_safe
from socios.models import Socio

class SocioAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'dni', 'pagos', 'ver']

    def pagos(self, obj):
        # return mark_safe( F'<a href="../../pagos/pago/?q={obj.dni}"> Pagos</a>' )
        return mark_safe( F'<a href="../../../pagos/create/{obj.id}" > Cargar Pago</a>' )

    def ver(self, obj):
        return mark_safe(F'<a href="../../../socios/show/{obj.id}" target="_blank"> Ver Completo</a>')

    search_fields = ['nombre', 'apellido', 'dni']

admin.site.register(Socio, SocioAdmin)
    
