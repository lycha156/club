from argparse import ONE_OR_MORE
from pyexpat import model
from django.db import models
from actividades.models import Actividad
from inscripciones.models import Inscripcion
from socios.models import Socio

class Pago(models.Model):
    # inscripcion = models.ForeignKey(Inscripcion, on_delete=models.RESTRICT, related_name="pago_inscripcion")
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="pago_socio");
    actividad = models.CharField("Actividad", max_length=50)
    fechapago = models.DateField("Fecha de Pago")
    comprobante = models.CharField("N° Comprobante Pago", null=True, blank=True, max_length=20)

    def __str__(self):
        return f"{self.socio.nombre}, {self.socio.apellido} ({self.actividad} - {self.fechapago})"
