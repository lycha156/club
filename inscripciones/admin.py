from django.contrib import admin

from .models import Inscripcion

class InscipcionAdmin(admin.ModelAdmin):
    fields = ['socio', 'actividad']
    list_display = ['socio', 'actividad']
    search_fields = ['socio__apellido', 'socio__nombre', 'actividad__actividad']
    autocomplete_fields = ['socio']
admin.site.register(Inscripcion, InscipcionAdmin)
