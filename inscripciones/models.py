from django.db import models
from socios.models import Socio
from actividades.models import Actividad

class Inscripcion(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="inscripcion_socio")
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name="inscripcion_actividad")
    
    class Meta:
        verbose_name_plural = "Inscripciones"

    def __str__(self):
        return F'{self.actividad.actividad} - {self.socio}'
